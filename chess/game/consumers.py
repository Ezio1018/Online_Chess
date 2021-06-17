from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Game
from .models import User

room=0
#self.scope类似于django中的request，包含了请求的type、path、header、cookie、session、user等等有用的信息
class GameConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):#连接时触发
        self.game_id = self.scope['url_route']['kwargs']['game_id']#拿出字典中的游戏id
        try: 
            self.game_id=int(self.game_id)
        except:
            await self.close()
            return
        side = await self.verify(self.game_id)
        print(side)
        if side == False:
            await self.close()
            return
        print(1)
        await self.accept()
        print(2)
        await self.join_room(side)
        print(3)

        if side[2]:
            await self.opp_online(side)

    async def receive_json(self, content):#从websocket接受指令
        command = content.get("command", None)#从command中拿
        try:
            if command == "new-move":#如果command是移动
                await self.new_move(content["source"],content["target"],content["fen"],content["pgn"])#从target中拿出起始位置和目标位置
            elif command == "game-over":#如果command是移动
                await self.game_over(content["result"],content["color"])#从target中拿出起始位置和目标位置
        except:
            pass
    
    async def disconnect(self, code):#取消连接
        await self.disconn()

    async def join_room(self, data):#加入房间

        await self.channel_layer.group_add(#
            str(self.game_id),
            self.channel_name,
        )
        await self.send_json({
            "command":"join",
            "orientation": data[0],
            "fen": data[1],
            "opp_online": data[2]
        })


    async def opp_online(self,data):
        await self.channel_layer.group_send(
            str(self.game_id),
            {
                "type": "online.opp",
                'sender_channel_name': self.channel_name,
                "name":data[3]
            }
        )
    
    async def online_opp(self,event):
        print(11111)
        if self.channel_name != event['sender_channel_name']:
            await self.send_json({
                "command":"opponent-online",
                "name":event["name"]
            })

    async def game_over(self, result, color):
        await self.channel_layer.group_send(#向频道房间发送移动棋子信息
            str(self.game_id),
            {
                "type": "over.game",
                "result": result,
                "color": color,
                'sender_channel_name': self.channel_name
            }
        )
    
    async def over_game(self, event):
        print(event['sender_channel_name'])
        print(self.channel_name)
        if self.channel_name != event['sender_channel_name']:
            await self.send_json({
                "command":"game-over",
                "result": event["result"],
                "color": event["color"],
            })
        await self.set_winner(event["color"])

    async def new_move(self, source, target,fen,pgn):
        print(source)
        await self.channel_layer.group_send(#向频道房间发送移动棋子信息
            str(self.game_id),
            {
                "type": "move.new",
                "source": source,
                "target": target,
                "fen": fen,
                "pgn": pgn,
                'sender_channel_name': self.channel_name
            }
        )
    
    async def move_new(self, event):
        print(event['sender_channel_name'])
        print(self.channel_name)
        if self.channel_name != event['sender_channel_name']:
            print(22222)
            await self.send_json({
                "command":"new-move",
                "source": event["source"],
                "target": event["target"],
                "fen": event["fen"],
                "pgn": event["pgn"],
            })
        await self.update(event["fen"],event["pgn"])

    @database_sync_to_async
    def verify(self, game_id):
        game = Game.objects.all().filter(id=game_id)[0]#从数据库找这场游戏
        if not game:
            return False
        userid = self.scope['url_route']['kwargs']['username']
        try:
            user = User.objects.get(user_id=userid)
        except:
            return False
        side = "white"
        opp=False
        print(game.opponent_id)
        if(game.opponent_id==None and userid!=game.owner_id):
            game.opponent_id=user.user_id
        if game.opponent_id == user.user_id:
            game.opponent_online = True
            if game.owner_side == "white":
                side = "black"
            else:
                side = "white"
            if game.owner_online == True:
                opp = True
            print("Setting opponent online")
        elif game.owner_id == user.user_id:
            game.owner_online = True
            if game.owner_side == "white":
                side = "white"
            else:
                side = "black"
            if game.opponent_online == True:
                opp = True
            print("Setting owner online")
        else:
            return False
        game.save()
        return [side,game.fen,opp,user.user_id]

    @database_sync_to_async
    def disconn(self):
        userid = self.scope['url_route']['kwargs']['username']
        try:
            user = User.objects.get(user_id=userid)
        except:
            return
        game = Game.objects.all().filter(id=self.game_id)[0]
        if game.opponent_id == user.user_id:
            game.opponent_online = False
            print("Setting opponent offline")
        elif game.owner_id == user.user_id:
            game.owner_online = False
            print("Setting owner offline")
        game.save()
        
    @database_sync_to_async
    def update(self, fen, pgn):
        game = Game.objects.all().filter(id=self.game_id)[0]
        if not game:
            print("Game not found")
            return
        game.fen = fen
        game.pgn = pgn
        game.status=2
        game.save()
        print("Saving game details")
    @database_sync_to_async
    def set_winner(self, color,):
        game = Game.objects.all().filter(id=self.game_id)[0]
        if not game:
            print("Game not found")
            return
        if(game.owner_side==color):
            game.winner=game.owner_id
        else:
            game.winner=game.opponent_id
        game.save()
        print("end game") 

