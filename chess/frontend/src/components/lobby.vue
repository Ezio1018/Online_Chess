<template>
  <div class="home">
    <el-row display="margin-top:10px">
      <el-input v-model="input_user_id" placeholder="请输入搜索用户编号"
                style="display:inline-table; width: 30%; float:left"></el-input>
      <el-button type="primary" @click="showGame()" style="float:left; margin: 2px;">搜索</el-button>
    </el-row>

    <el-row>
      <el-table :data="gamelist" style="width: 100%" border>

        <el-table-column label="房主" min-width="100">
          <template slot-scope="scope"> {{ scope.row.owner_id }}</template>
        </el-table-column>
        <el-table-column label="颜色" min-width="100">
          <template slot-scope="scope"> {{ scope.row.owner_side }}</template>
        </el-table-column>
        <el-table-column label="时间" min-width="100">
          <template slot-scope="scope"> {{ scope.row.time }}</template>
        </el-table-column>
        <el-table-column label="状态" min-width="100">
          <template slot-scope="scope"> {{ scope.row.status }}</template>
        </el-table-column>
        <el-table-column label="操作" min-width="100">
          <template slot-scope="scope"><!--作用域插槽-->
            <el-button type="primary" icon="el-icon-check" size="mini" @click="joinGame(scope.row.id)"></el-button>
          </template>
        </el-table-column>

      </el-table>
    </el-row>

  </div>
</template>

<script>
  export default {
    name: 'home',
    data () {
      return {
        input_user_id: '',
        gamelist: [],
      }
    },
    mounted: function () {
      this.showGame()
    },
    methods: {
      joinGame(pk){
          this.$router.push({path: '/game'});
          localStorage.id = pk;
          localStorage.guest=true;
          window.location.reload();
      },
      showGame () {
        this.$http.get('http://127.0.0.1:8000/api/show_game?user_id=' + this.input_user_id)
          .then((response) => {
            var res = JSON.parse(response.bodyText)
            console.log(res)
            if (res.error_num === 0) {
              this.gamelist = res['list']
              
              
            } else {
              this.$message.error('查询房间失败')
              console.log(res['msg'])
            }
          })
      },
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  a {
    color: #42b983;
  }
</style>
