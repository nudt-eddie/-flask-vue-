<template>
  <div class="search" >
    <div class="info" >
      <div v-show="isShow">
      <div class="avator">
      <img :src="this.$res_data_user.avatar_url"  alt="用户头像" />
      </div>
      <el-divider ></el-divider>
    <el-descriptions
      class="margin-top"
      title="个人信息"
      :column="3"
      :size="size"
      border
      v-loading="loading"
      style="width: 100%"
    >
      <el-descriptions-item class-name="usrname">
        <template slot="label">
          <i class="el-icon-user"></i>
          用户名
        </template>
        {{this.$res_data_user.usname}}
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-female"></i>
          性别
        </template>
        {{this.$res_data_user.gender}}
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-cherry"></i>
          生日
        </template>
        {{this.$res_data_user.birth}}
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-map-location"></i>
          地址
        </template>
        {{this.$res_data_user.address}}
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-alarm-clock"></i>
          创建时间
        </template>
        {{ this.$res_data_user.time }}
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-wind-power"></i>
          微博数量
        </template>
        {{this.$res_data_user.counts}}
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-potato-strips"></i>
          粉丝数
        </template>
        {{ this.$res_data_user.fans }}
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-pear"></i>
          关注数
        </template>
        {{ this.$res_data_user.friends }}
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-position"></i>
          微号
        </template>
        {{ this.$res_data_user.id }}
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-mic"></i>
          微博认证信息
        </template>
        {{ this.$res_data_user.des }}
      </el-descriptions-item>
      <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-medal"></i>
          简介
        </template>
        {{this.$res_data_user.pro}}
      </el-descriptions-item>
            <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-medal"></i>
          所在地
        </template>
        {{this.$res_data_user.ip_location}}
      </el-descriptions-item>
            <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-medal"></i>
          教育信息
        </template>
        {{this.$res_data_user.school}}
      </el-descriptions-item>
          <el-descriptions-item>
        <template slot="label">
          <i class="el-icon-medal"></i>
          链接地址
        </template>
        {{"https://weibo.com" + this.$res_data_user.profile_url}}
      </el-descriptions-item>
    </el-descriptions>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isShow: true,
    };
  },
  methods: {
  },
};
</script>

<style scoped>

  .avator {
    /* 宽度 */
    width: 150px;
    /* 高度 */
    height: 150px;
    /* 属性定位 */
    position:relative;
    /* 属性定位，顶部占比 */
    top: 30px;
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
  .avator img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
    background: rgb(238, 238, 238);
  }
</style>