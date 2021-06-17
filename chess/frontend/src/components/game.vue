<template>
  <div id="chess">
    <!-- <chessboard @onMove="showInfo"/> -->
  <div id="left">
	<h1> 黑方 </h1>
	<h1> {{ left }} </h1>
  <h1>——VS——</h1>
	<h1> 白方 </h1>
	<h1> {{ right }} </h1>
	</div>
    <newboard ref="time"></newboard>
    </div>
</template>
<script>
import 'vue-chessboard/dist/vue-chessboard.css'
import newboard from './newboard.vue'
export default {
  name: 'chess',
  components: {
    newboard,
  },

  data () {
    return {
      left:'00:00',
      right:'00:00',
      lLeftTime: localStorage.time *60* 1000,
      rLeftTime:  localStorage.time * 60 * 1000,
      flag: 1,
      show:true,
      currentFen: '',
      positionInfo: null,
      message: "",
      toFather:""
    }
  },
  mounted(){
    this.$refs['time'].$on('func',(msg)=>{
                console.log(msg);
                if(msg=='white'){
                  this.flag = 2
                  this.leftCountDown()
                }
                else
                {
                  this.flag = 1
                  this.rightCountDown()
                }

            })
  },
  methods: {
      
    leftCountDown(){
      this.lLeftTime = this.lLeftTime  - 100;
      //定义变量 d,h,m,s保存倒计时的时间
      if (this.lLeftTime >= 0) {
        this.d = Math.floor(this.lLeftTime / 1000 / 60 / 60 / 24);
        this.h = Math.floor(this.lLeftTime / 1000 / 60 / 60 % 24);
        this.m = Math.floor(this.lLeftTime / 1000 / 60 % 60);
        this.s = Math.floor(this.lLeftTime / 1000 % 60);
      }
      if(this.lLeftTime==0){
         this.$notify({
                  title: "白方胜利",
            });
          this.$router.push({path: '/home'});
          localStorage.id = 0
          window.location.reload();
      }
      if(this.flag % 2 == 0 && this.lLeftTime > 0) {
        setTimeout(this.leftCountDown, 100);	
          }
      this.left = this.h + ':' + this.m + ':' + this.s
      

    },
    
    rightCountDown(){
      this.rLeftTime = this.rLeftTime  - 100;
      //定义变量 d,h,m,s保存倒计时的时间
      if (this.rLeftTime >= 0) {
        this.d = Math.floor(this.rLeftTime / 1000 / 60 / 60 / 24);
        this.h = Math.floor(this.rLeftTime / 1000 / 60 / 60 % 24);
        this.m = Math.floor(this.rLeftTime / 1000 / 60 % 60);
        this.s = Math.floor(this.rLeftTime / 1000 % 60);
      }
      
       if(this.lLeftTime==0){
         this.$notify({
                  title: "黑方胜利",
              });
          this.$router.push({path: '/game'});
          localStorage.id = 0
          window.location.reload();
      }
      if(this.flag % 2 == 1 && this.rLeftTime > 0) {
        setTimeout(this.rightCountDown, 100);	
          }
      
      this.right = this.h + ':' + this.m + ':' + this.s
    },
      
    copyText(){
        this.show=false;
    },
    showInfo(data) {
      this.positionInfo = data;
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
        this.time=localStorage.time;
        console.log(localStorage.time)
        this.isonline=localStorage.isonline;
        this.user_id = localStorage.user_id;
        // this.lLeftTime= this.time *60* 1000;
        // this.rLeftTime= this.time * 60 * 1000;
    },
}
</script>
<style scoped>
  #left{
    position:relative;
   font-size:42;
    left:9%;
    top:20%;
      display: flex;

  }  
</style>