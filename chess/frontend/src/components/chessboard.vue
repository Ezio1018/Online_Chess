<template>
  <div id="chess">
    <h1>Simple Chessboard with legal moves</h1>
    <!-- <chessboard @onMove="showInfo"/> -->
    <newboard/>
    <div>
    {{this.positionInfo}}
  </div>
  </div>
</template>
<script>
import {chessboard} from 'vue-chessboard'
import 'vue-chessboard/dist/vue-chessboard.css'
import newboard from './newboard.vue'
export default {
  name: 'chess',
  components: {
    chessboard,
    newboard,
  },
  data () {
    return {
      currentFen: '',
      positionInfo: null,
      message: "",
    }
  },
  mounted: function() {
      this.initWebSocket();
    },
  methods: {
    initWebSocket() {
      var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
      var ws_path = ws_scheme + "://localhost:8000/game/1/zgf";
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
        console.log("joining room as "+data.orientation)
        var config = {
        onDrop: onDrop,
        orientation: data.orientation
        }
        board = Chessboard('myBoard', config)
        game.load_pgn(data.pgn)
        board.position(game.fen());
      }
      else if(data.command=="opponent-online"){
       
      }
      else if(data.command=="new-move") {
        game.move({
            from: data.source,
            to: data.target
          });
        board.position(game.fen());
      }
    },
    websocketsend(Data){//数据发送
      this.websock.send(Data);
    },
    websocketclose(e){  //关闭
      console.log('断开连接',e);
    },
    showInfo(data) {
      this.positionInfo = data;

      socket.send(JSON.stringify({"command": "new-move","source": source,"target": target,"fen": game.fen(), "pgn": game.pgn()}));
    },
    loadFen(fen) {
      this.currentFen = fen
    },
    promote() {
      if (confirm("Want to promote to rook? Queen by default") ) {
        return 'r'
      } else {
        return 'q'
      }
    }
  },
  created() {
    this.fens = ['5rr1/3nqpk1/p3p2p/Pp1pP1pP/2pP1PN1/2P1Q3/2P3P1/R4RK1 b - f3 0 28',
                'r4rk1/pp1b3p/6p1/8/3NpP2/1P4P1/P2K3P/R6R w - - 0 22'
                ]
  }
}
</script>