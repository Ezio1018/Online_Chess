<script>
import { chessboard }  from 'vue-chessboard'
export default {
  name: 'justboard',
  extends: chessboard,
}
</script>
<style scoped>
.cg-board-wrap {
  width: 600px;
  height: 600px;
  /* left: 25%; */
   /* margin: 0 auto; */
  position: relative;
  display: block;
}
</style>