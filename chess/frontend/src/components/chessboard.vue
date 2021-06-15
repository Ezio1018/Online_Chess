<template>
  <div id="chess">
    <!-- <h1>Simple Chessboard with legal moves</h1> -->
    <!-- <chessboard @onMove="showInfo"/> -->
    <justboard/>
    <div class="btns">
       <el-button type="success" size="big" @click="addDialogVisible = true;ismobile=false" >创建电脑端房间</el-button>
      
       <el-button type="success" size="big" @click="addDialogVisible = true;ismobile=true" >创建手机端房间</el-button>
    </div>
  
    <el-dialog
                title="添加房间"
                :visible.sync="addDialogVisible"
                width="40%"
                @close="addDialogClosed">
            <!--:before-close="handleClose">-->
            <!--内容主体区域,ref是引用对象名-->
            <el-form :model="addForm" ref="addFormRef" label-width="70px">
                <!-- <el-form-item label="指定对手">
                    <el-input v-model="addForm.opponentid"></el-input>
                </el-form-item> -->
                <el-form-item label="对局时间" >
                    <el-select v-model="addForm.time" style="display: block;">
                        <el-option label="3min" value="3"></el-option>
                        <el-option label="5min" value="5"></el-option>
                        <el-option label="10min" value="10"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="悔棋" >
                     <el-select v-model="addForm.regret" style="display: block;">
                        <el-option label="是" value="1"></el-option>
                        <el-option label="否" value="0"></el-option>
                    </el-select>
                </el-form-item>
                <el-form-item label="颜色" >
                     <el-select v-model="addForm.color" style="display: block;">
                        <el-option label="执黑" value="black"></el-option>
                        <el-option label="执白" value="white"></el-option>
                    </el-select>
                </el-form-item>
            </el-form>
            <!--底部按钮区-->
            <span slot="footer" class="dialog-footer">
                <el-button @click="addDialogVisible = false">取 消</el-button><!--点击取消隐藏对话框-->
                <el-button type="primary" @click="submit">确 定</el-button><!--点击确定也会隐藏对话框-->
            </span>
        </el-dialog>
  </div>

</template>
<script>
import 'vue-chessboard/dist/vue-chessboard.css'
import justboard from './justboard.vue'
export default {
  name: 'chess',
  components: {
    justboard,
  },
  data () {
    return {
      ismobile:false,
      currentFen: '',
      positionInfo: null,
      message: "",
      addForm:{
                opponentid:"",
                time:"",
                regret:"",
                color:"",
              },
      addDialogVisible:false,
        addFormRules: {
                   
                   
                },//添加表单的验证规则对象
    }
  },
  methods: {

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
    },
     submit(){
            let formData = new FormData();
            formData.append('userid', this.user_id);
            // formData.append('opponentid', this.addForm.opponentid);
            formData.append('time', this.addForm.time);
            formData.append('regret', this.addForm.regret);
            formData.append('color', this.addForm.color);
          // 成功.
          this.$axios.post('http://127.0.0.1:8000/api/room', formData)
            .then(response => {
              if (response.data.status === 0) {
                this.$notify({
                  title: '创建成功',
                  message: response.data.message,
                  type: 'sucess'
                });
                if(this.ismobile){
                this.$router.push({path: '/mobilegame'});
                }
                else{
                this.$router.push({path: '/game'});
                }
                localStorage.id = response.data.id
                localStorage.time = this.addForm.time
                window.location.reload();
              } else {
                return false
              }
            })
    },
      addDialogClosed(){
              this.$refs.addFormRef.resetFields()
          },
  },
  mounted(){

  },
  created() {
    this.ismobile=false;
    this.user_id = localStorage.user_id;
  },

     

}
</script>
<style scoped>
    
    .btns{
        position:relative;/*可以用坐标标记*/
        /* height:50px; */
        /* width:100px; */
        left: 170px;
        display: flex;
        /* justify-content: flex-end; */
    }
</style>
