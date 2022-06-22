<template >
  <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    <el-menu :default-openeds="['1', '3']" :router="true"  style="background-color: rgb(238, 241, 246)" >
        <el-menu-item-group>
          <el-menu-item :index="this.menuList.a.path" style="background-color: rgb(238, 241, 246)">目标搜索</el-menu-item>
          <el-menu-item :index="this.menuList.b.path" style="background-color: rgb(238, 241, 246)">个人信息</el-menu-item>
          <el-menu-item :index="this.menuList.c.path" style="background-color: rgb(238, 241, 246)">人际关系</el-menu-item>
          <el-menu-item :index="this.menuList.d.path" style="background-color: rgb(238, 241, 246)">微博动态</el-menu-item>
          <el-menu-item :index="this.menuList.e.path" style="background-color: rgb(238, 241, 246)">微博评论</el-menu-item>
        </el-menu-item-group>
    </el-menu>
  </el-aside>
</template>

<script>
  export default {
    name: "Navigation",
    data() {
      return {
        menuList:{
          a: {
            id: 1,
            path: "/home/start"
          },
          b: {
            id: 1,
            path: "/home/user"
          },
          c: {
            id: 2,
            path: "/home/relation"
          },
          d: {
            id: 3,
            path: "/home/statuses"
          },
          e: {
            id: 4,
            path: "/home/comments"
          }
        }
      }
    }
  };
</script>

<style>
  .el-menu-vertical-demo:not(.el-menu--collapse) {
    width: 200px;
    min-height: 400px;
  }
</style>
