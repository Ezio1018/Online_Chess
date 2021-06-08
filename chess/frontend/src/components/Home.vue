<template>
    <el-container class="home-container">
        <el-header>会议室
            <template>
                <el-dropdown class="profileLoc">
                        <span class="el-dropdown-link">
                            <img src="../../src/assets/我的.png"/>
                            <i class="el-icon-arrow-down el-icon--right"></i>
                        </span>
                    <el-dropdown-menu slot="dropdown">
                        <el-dropdown-item style="font-size:20px">查看个人信息</el-dropdown-item>
                        <el-dropdown-item style="font-size:20px">退出</el-dropdown-item>
                    </el-dropdown-menu>
                </el-dropdown>
            </template>
        </el-header>
        <el-container>
            <el-aside width="200px" style="background:rgba(255,255,255,0.5);">
                <el-card>
                    <el-menu v-on:unique-opened="true"
                             background-color=""
                             text-color="black"
                             active-text-color="blue" unique-opened router><!--这个是选中的时候显示的颜色-->
                        <el-menu-item index="/firsthop" @click="saveNavState('/'+$route.path)">
                            <i class="el-icon-menu"></i>
                            <span slot="title" >首页</span>
                        </el-menu-item>
                      <el-menu-item index="/chessboard" @click="saveNavState('/'+$route.path)">
                        <i class="el-icon-menu"></i>
                        <span slot="title" >下棋</span>
                      </el-menu-item>
               </el-menu>
                </el-card>
            </el-aside>
            <el-container >
                <el-main style="background:rgba(255,255,255,0.5);">
                    <!--路由占位符-->
                    <!--在router的index.js里面实现，这里跳转到firsthop页面-->
                    <el-card>
                        <router-view></router-view>
                    </el-card>
                </el-main>
            </el-container>
        </el-container>
    </el-container>

</template>
<script>
export default {
  name: 'home',
    methods:{
        saveNavState (activepath){ // 为每一个按钮添加，按下去的时候会在Application里面加入一个activepath
      window.sessionStorage.setItem('activepath', activepath)// 用来保存当前访问的路径
    }
    }
}
</script>

<style scoped>
    .el-header{
        background-color: white;
        font-size:20px;

    }
    .el-aside{
        background: linear-gradient(135deg,white,white);
    }
    .el-menu{
        border-right:none;/*解决2级菜单突出来的情况*/
    }
    .el-main{
        background-color: white;
    }
    .home-container{
        height: 100vh;
        background: url('../../src/assets/nastuh-abootalebi-eHD8Y1Znfpk-unsplash.jpg')  no-repeat scroll top right  #aaa9a7;
        background-size: cover;

    }
    .el-header{
        font-family :"幼圆";
        font-size :40px;
    }
    .profileLoc{
        position:absolute;/*可以用坐标标记*/
        top: 0.5%;
        right: 1%;
    }
    .el-dropdown-link {

        cursor: pointer;
        color: white;
    }
    .el-icon-arrow-down {
        font-size: 25px;
    }
</style>
