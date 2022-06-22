<template>
  <el-container>
    <div class="imgUrl">
      <div class="titleText">微博爬虫</div>
      <div class="btn">
        <el-button @click="loginOut">退出</el-button>
      </div>
      <!--div class="block"><el-avatar :size="50" :src= "this.$res_data_user.avatar_url"    ></el-avatar></div-->
    </div>
  </el-container>

</template>

<script>
export default {
  name: "Header",
  data() {
    return { 

      };
  },
  methods: {
    loginOut() {
      this.$router.push("/login");
    },
  },
};
</script>

<style>
.el-header {
  line-height: 50px;
  color: rgb(248, 243, 243);
  font-size: 20px;
}

.el-header img {
  vertical-align: middle;
}

.imgUrl {
  background: linear-gradient(
    to right,
    #a00303,
    #525252
  ); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

  background-size: 100%;
  width: 100%;
}

.titleText {
  float: left;
  margin-left: 20px;
}

.btn {
  float: right;
  margin-right: 20px;
}
.block {  
    float: right;
    margin-right: 20px;

}
</style>
