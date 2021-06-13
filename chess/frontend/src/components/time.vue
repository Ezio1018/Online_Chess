<script src="https://cdn.jsdelivr.net/npm/vue"></script>
<script src="http://code.jquery.com/jquery-2.0.0.min.js"></script>
<template>


<div id="this">

	<div id="left" style="margin-left:5%;float:left;font-size:42">
	<h1>正方</h1>
	<h1>剩余时间 {{ left }} </h1>
	</div>

	<div id="right" style="margin-right:5%;float:right;font-size:42">
	<h1>反方</h1>
	<h1>剩余时间 {{ right }} </h1>
	</div>

	<div style="float:left">
	<el-button type="primary" @click="start">确 定</el-button><!--点击确定也会隐藏对话框-->
	</div>

</div>
	
</template>
<script>
export default {
  data() {
	return{
    left:'00:05:00',
    right:'00:05:00',
    lLeftTime: 5 * 60 * 1000,
    rLeftTime: 5 * 60 * 1000,
    flag: 1,
	  }
  },

  methods:{
 
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
	}
  }
}
</script>
