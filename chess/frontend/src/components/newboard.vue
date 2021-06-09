<script>
import { chessboard }  from 'vue-chessboard'
export default {
  name: 'newboard',
  extends: chessboard,
  methods: {
    userPlay() {
      return (orig, dest) => {
        console.log(this.c);
        console.log(this.toColor());
        if(this.c==this.toColor()){
        if (this.isPromotion(orig, dest)) {
          this.promoteTo = this.onPromotion();
        }
        this.game.move({from: orig, to: dest, promotion: this.promoteTo}) // promote to queen for simplicity
        this.board.set({
          fen: this.game.fen(),
          turnColor: this.toColor(),
          movable: {
            color: this.toColor(),
            dests: this.possibleMoves(),
          },
        })
        this.socket.send(JSON.stringify({"command": "new-move","source": orig,"target": dest,"fen": this.game.fen(), "pgn":this.game.pgn()}));
        this.calculatePromotions();
      }
      else{
         this.board.set({
          fen: this.game.fen(),
          turnColor: this.toColor(),
          movable: {
            color: this.toColor(),
            dests: this.possibleMoves(),
          },
        })
      }
      };
    },
    NextMove(orig,dest) {
      console.log("对手下棋")
        this.game.move({from: orig, to: dest, promotion: this.promoteTo}) // promote to queen for simplicity
        this.board.set({
          fen: this.game.fen(),
          turnColor: this.toColor(),
          movable: {
            color: this.toColor(),
            dests: this.possibleMoves(),
          },
        })
    },
    initWebSocket() {
      var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
      var ws_path = ws_scheme + "://127.0.0.1:8000/game/1/"+this.user_id;
      console.log(ws_path);
      this.socket = new WebSocket(ws_path);
      this.socket.onmessage = this.websocketonmessage;
      this.socket.onopen = this.websocketonopen;
      // this.socket.onerror = this.websocketonerror;
      this.socket.onclose = this.websocketclose;
    },
    websocketonopen(){ //连接建立之后执行send方法发送数据
      console.log('success');
    },
    websocketonerror(){//连接建立失败重连
      this.initWebSocket();
    },
    websocketonmessage(message){ //数据接收
      console.log("Got websocket message " + message.data);
      var data = JSON.parse(message.data);
      if (data.command=="join") {
        this.c=data.orientation;
      this.board.set({
      orientation:data.orientation,
       movable: { events: { after: this.userPlay() } },
      })
        console.log("joining room as "+data.orientation)
      }
      else if(data.command=="opponent-online"){
        console.log("opponent join the room");
      }
      else if(data.command=="new-move") {
          this.NextMove(data.source, data.target);
      }
    },
    websocketsend(Data){//数据发送
      this.socket.send(Data);
    },
    websocketclose(e){  //关闭
      console.log('断开连接',e);
    },
  },
  created(){
       this.user_id = localStorage.user_id;
       this.c="white";
  },
  mounted() {
    this.initWebSocket();
    
  }
}
</script>