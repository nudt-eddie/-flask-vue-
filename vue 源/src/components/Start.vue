<template>
  <div class="box">
    <div class="login_logo">
      <img src="../assets/nlogo.png" alt="" />
    </div>
    <el-input
      placeholder="请输入内容"
      v-model="searchNameForm.uname"
      class="input-with-select"
    >
      <el-select v-model="select" slot="prepend" placeholder="请选择">
        <el-option label="用户名" value="1"></el-option>
        <el-option label="uid" value="2"></el-option>
      </el-select>
    </el-input>
    <div class="button">
      <el-button class="butn"  @click="start">爬取</el-button>
    </div>
    <div>
      <el-dialog
        title="提示"
        :visible.sync="centerDialogVisible"
        width="30%"
        center
      >
        <div style="text-align: center">
          <el-progress
            type="line"
            :percentage="percentage"
            :status="success"
          ></el-progress>
          <p style="color: teal">{{ messages }}</p>
        </div>
        <span slot="footer" class="dialog-footer">
          <el-button @click="centerDialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="centerDialogVisible = false"
            >确 定</el-button
          >
        </span>
      </el-dialog>
    </div>
  </div>
</template>

<script>
import Vue from "vue";
export default {
  data() {
    return {
      success: "",
      messages: "",
      searchNameForm: {
        uname: "",
      },
      select: "",
      centerDialogVisible: false,
      percentage: 0,
    };
  },
  mounted() {
    this.note();
  },
  methods: {
    note() {
      const h = this.$createElement;
      this.$notify.info({
        title: "注意",
        message: h(
          "i",
          { style: "color: teal" },
          "用户搜索默认为第一个结果,若进度条没有动静,请重新登录更新coookie!"
        ),
        position: "bottom-right",
        duration: 5000,
      });
    },
    increase() {
      this.percentage += 10;
      if (this.percentage >= 100) {
        this.percentage = 100
        this.success = "success"
      }
    },
    async getInfo() {
      this.increase();
      this.messages = "正在爬取目标信息...";
      const params = this.qs.stringify(this.searchNameForm);
      await this.$axios.post("/api/search", params).then((res) => {
        Vue.prototype.$res_data_user = res.data;
        this.increase();
      });
    },
    async getStatuses() {
      this.increase();
      this.messages = "正在爬取微博动态...";
      await this.$axios.get("/api/statuses").then((res) => {
        Vue.prototype.$res_data_statuses = res.data.data.list;
        this.increase();
      });
    },
    async getRelation() {
      this.increase();
      this.messages = "正在生成关系视图...";
      await this.$axios.get("/api/friends").then((res) => {
        Vue.prototype.$res_data_friends = res.data.users;
        this.increase();
      });
      await this.$axios.get("/api/fans").then((res) => {
        this.increase();
        Vue.prototype.$res_data_fans = res.data.users;
        this.increase();
      });
    },
    async getComments(){
      this.increase();
      this.messages = "正在获取评论...";
      await this.$axios.get("/api/comments").then((res) => {
          localStorage.setItem('COMMENTS', JSON.stringify(res.data))
          this.increase();
          this.messages = "爬取成功!";
      });
    },

    supervise(){
      console.log("check for supervise")
      this.$axios.get("/api/check").then((res) => {
        if (res.data != -1){
          Vue.prototype.$res_data_statuses = res.data.data.list;
          const h = this.$createElement;
          this.$notify.info({
            title: "提示",
            message: h(
              "i",
              { style: "color: teal" },
              "检测到目标用户动态已更新, 请及时查看!"
            ),
            position: "bottom-left",
            duration: 5000,
          });
        }
        else{
          const h = this.$createElement;
          this.$notify.info({
            title: "提示",
            message: h(
              "i",
              { style: "color: teal" },
              "目标用户动态无变化, 请稍后..."
            ),
            position: "bottom-left",
            duration: 5000,
          });
        }
      });      
    },
    async start(){
      this.centerDialogVisible = true;
      await this.getInfo();
      await this.getStatuses();
      await this.getRelation();
      await this.getComments();
      setInterval(this.supervise,30000);
    }
  },
};
</script>


<style>
.el-select .el-input {
  width: 130px;
}
.input-with-select .el-input-group__prepend {
  background-color: #fff;
}
.box {
  width: 50%;
  position: absolute;
  bottom: 400px;
  right: 200px;
  left: 400px;
  /* 边框边距 */
}
.button {
  position: absolute;
  bottom: -50px;
  right: 200px;
  left: 200px;
}
.butn{
  background-image: linear-gradient(-225deg, #7DE2FC 0%, #B9B6E5 100%);
}
.login_logo img {
  width: 40%;
  height: 40%;

  background: rgb(255, 255, 255);
}
</style>