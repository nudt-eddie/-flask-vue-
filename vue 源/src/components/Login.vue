<template>
  <div class="login">
    <div class="login_title">
      <div class="login_context">
        
        <!-- 这里放图片logo -->
        <div class="login_logo">
          <img src="../assets/logo.png" alt="" />
          
        </div>
        <el-form :model="loginRuleForm" :rules="loginRules" ref="loginRules" class="login_box">

          <el-form-item label="账号" prop="username">
            <el-input v-model="loginRuleForm.username"></el-input>
          </el-form-item>

          <el-form-item label="密码" prop="password">
            <el-input v-model="loginRuleForm.password" show-password></el-input>
          </el-form-item>

          <el-form-item class="btns">
            <el-button type="primary" @click="login">登陆</el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>
  </div>
</template>



<script>
  // Vue 代码逻辑
  export default {
    
    data() {
      return {
        // 表单请求数据
        loginRuleForm: {
          username: '',
          password: '',
        },
        // 表单验证规则
        loginRules: {
          username: [{
              required: true,
              message: "请输入账号",
              trigger: "blur"
            },
            {
              min: 3,
              max: 18,
              message: "长度在 3 到 18 个字符",
              trigger: "blur",
            },
          ],
          password: [{
              required: true,
              message: "请输入密码",
              trigger: "blur"
            },
            {
              min: 3,
              max: 18,
              message: "长度在 3 到 18 个字符",
              trigger: "blur",
            }
          ]
        }
      };
    },
    methods: {
      login() {
        // 登陆进行规则的校验，只有校验成功才能登陆
        // vaild=>所有的规则校验都成立才会进入到这里
        this.$refs.loginRules.validate((vaild) => {
          if (!vaild) return;
          // 直接请求数据，格式是payload，如果服务端要求是payload格式那么这样请求
          // this.$axios.post("http://192.168.17.176:8089/login", this.loginRuleForm).then((res) => {
          //   console.log(res)
          // })
          const loading = this.$loading({
            lock: true,
            text: '登陆中, 请在微博手机端中确认',
            spinner: 'el-icon-loading',
            background: 'rgba(0, 0, 0, 0.7)'
          })

          // 请求数据，格式是formdata，需要添加 this.qs.stringify()进行格式转换
          const params = this.qs.stringify(this.loginRuleForm)
          this.$axios.post("/api/checklogin", params).then((res) => {
            console.log(res)
            // if (res.data.code != 0 && res.data.code != 401) {
            //   return this.$message.error(res.data.msg);
            // }
            if (res.data == 0){
              loading.close()
              this.$message.success("Hi " + this.loginRuleForm.username + " 登录成功!")
              return this.$router.push("/home/start"); // 跳转到搜索主页
            }
            else{
              loading.close()
              return this.$message.error("登录失败,请重新登录!")
            }

          })
        })
      }
    },

  }
  
</script>

<style scoped>

  .login {
    /* 高度 */
    height: 100%;
    /* 背景色*/ 
    background: url(../assets/index.jpg)
    /*linear-gradient(
    to right,
    #ee0606,
    #525252
    );*/

  }

  .login_title {
    /* 字体水平左右居中 */
    text-align:center;
  }
  .login_context {
    /* 宽度 */
    width: 450px;
    /* 高度 */
    height: 350px;
    /* 背景色 */
    background: #fff;
    /* 属性定位 */
    position: absolute;
    /* 属性定位，顶部占比 */
    top: 50%;
    /* 属性定位，左侧占比 */
    left: 50%;
    /* 水平垂直居中 */
    transform: translate(-50%, -50%);
    /* 四个角的圆角角度 */
    border-radius: 20px;
    /* 阴影 */
    box-shadow: 0 0 5px 2px #ddd;
  }

  .login_logo {
    /* 宽度 */
    width: 150px;
    /* 高度 */
    height: 150px;
    /* 属性定位 */
    position: absolute;
    /* 属性定位，顶部占比 */
    top: -150px;
    /* 属性定位，左侧占比 */
    left: 49%;
    /* logo左侧边距 */
    margin-left: -75px;
    /* 带有边框属性 */
    border: 1px solid rgb(255, 255, 255);
    /* 四个角的圆角角度 */
    border-radius: 50%;
    /* 背景色 */
    background: rgb(255, 255, 255);
    /* 设置内边距属性 */
    padding: 10px;
    /* 阴影 */
    box-shadow: 0 0 2px 2px rgb(255, 255, 255);
  }

  .login_logo img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: rgb(238, 238, 238);
  }

  .login_box {
    width: 100%;
    position: absolute;
    bottom: 0px;
    padding: 0 50px;
    /* 边框边距 */
    box-sizing: border-box;
  }

  .btns {
    /* 将对象作为弹性伸缩盒显示 */
    display: flex;
    /* 横轴方向上的对齐方式 */
    justify-content: center;
  }

</style>
