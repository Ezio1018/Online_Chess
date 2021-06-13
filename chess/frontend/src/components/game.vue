<template>
  <div id="chess">
        <!-- <el-button type="primary"  @click="copyText">注册</el-button> -->
        <h1 v-if="show">等待对手加入房间。。。。。。</h1>
    <!-- <chessboard @onMove="showInfo"/> -->
  <div id="left">
	<h1> {{ left }} </h1>
	</div>

	<div id="right">
	<h1> {{ right }} </h1>
	</div>
    <newboard/>

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
      left:'05:00',
      right:'05:00',
      lLeftTime: 5 * 60 * 1000,
      rLeftTime: 5 * 60 * 1000,
      flag: 1,
      show:true,
      currentFen: '',
      positionInfo: null,
      message: "",
      toFather:""
    }
  },
  methods: {
      
    leftCountDown(){
      this.lLeftTime = this.lLeftTime  - 1000;
      //定义变量 d,h,m,s保存倒计时的时间
      if (this.lLeftTime >= 0) {
        this.d = Math.floor(this.lLeftTime / 1000 / 60 / 60 / 24);
        this.h = Math.floor(this.lLeftTime / 1000 / 60 / 60 % 24);
        this.m = Math.floor(this.lLeftTime / 1000 / 60 % 60);
        this.s = Math.floor(this.lLeftTime / 1000 % 60);
      }
      
      if(this.flag % 2 == 0 && this.lLeftTime > 0) {
        setTimeout(this.leftCountDown, 1000);	
          }
      
      this.left = this.h + ':' + this.m + ':' + this.s
      

    },
    
    rightCountDown(){
      this.rLeftTime = this.rLeftTime  - 1000;
      //定义变量 d,h,m,s保存倒计时的时间
      if (this.rLeftTime >= 0) {
        this.d = Math.floor(this.rLeftTime / 1000 / 60 / 60 / 24);
        this.h = Math.floor(this.rLeftTime / 1000 / 60 / 60 % 24);
        this.m = Math.floor(this.rLeftTime / 1000 / 60 % 60);
        this.s = Math.floor(this.rLeftTime / 1000 % 60);
      }
      
      
      if(this.flag % 2 == 1 && this.rLeftTime > 0) {
        setTimeout(this.rightCountDown, 1000);	
          }
      
      this.right = this.h + ':' + this.m + ':' + this.s
    },
      
    start(){
      this.flag += 1
      if(this.flag % 2 == 0){
        this.leftCountDown()
          }
      else{
        this.rightCountDown()
          }	
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
        this.isonline=localStorage.isonline;
        if(localStorage.guest){
          this.show=false;
        }
        this.user_id = localStorage.user_id;
    },
}
</script>
<style scoped>
  #left{
    position:absolute;
   font-size:42;
    left:35%;
    top:20%;
  }
  #right{
    position:absolute;
   font-size:42;
    left:35%;
    bottom:40%;
  }
</style>