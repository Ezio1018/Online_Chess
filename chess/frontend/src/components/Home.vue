<template>
<div class="home">
<el-menu
  v-on:unique-opened="true"
  :default-active="activeIndex"
  class="el-menu-demo"
  mode="horizontal"
  @select="handleSelect"
  background-color="#545c64"
  text-color="#fff"
  active-text-color="#ffd04b"
  unique-opened router>
  <el-menu-item index="/firsthop">首页</el-menu-item>
  <el-menu-item index="/chessboard">下棋</el-menu-item>
  <el-menu-item index="/lobby">大厅</el-menu-item>
  <el-menu-item index="/game" :disabled="this.hasGame==false">对局</el-menu-item>

</el-menu>
<el-container >
    <el-main style="background:rgba(255,255,255,0.5);">
        <!--路由占位符-->
        <!--在router的index.js里面实现，这里跳转到firsthop页面-->
        <el-card style="background:#fcfdf8;">
            <router-view></router-view>
        </el-card>
    </el-main>
</el-container>
</div>
</template>
<script>
  export default {
    data() {
      return {
        hasGame:false,
        activeIndex: '1'
      };
    },
    methods: {
        
      handleSelect(key, keyPath) {
          this.$router.push({path: keyPath,});
      }
    }
    
  }
</script>

<style scoped>

    /* .home{
        background: url('../../src/assets/chess.jpg')  no-repeat scroll top right  #aaa9a7;
        background-size: cover;

    } */
</style>
