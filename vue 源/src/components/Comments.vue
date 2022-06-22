<template>
    <el-collapse accordion>
    <el-collapse-item
        v-for="(statuse,index) in this.$res_data_statuses.slice(0,10)"
        :key="statuse"
    >
        <template slot="title">
        <div style="color: teal">{{ statuse.text_raw }}</div>
        </template>
        <div v-for="(item) in comments[index].slice(0,10)"
        :key="item"
        >
        <h4> 用户名: {{item.name}} </h4>
        <h4> uid: {{item.id}} </h4>
        <h4 v-html='item.text'></h4>
        <h4> 点赞: {{item.likes}} 时间: {{item.time}} </h4>
        <el-divider ></el-divider>
        </div>
    </el-collapse-item>
    </el-collapse>
</template>

<script>
export default {
  data() {
    return {
      comments: JSON.parse(localStorage.getItem('COMMENTS')),
      activeNames: ["1"],
    };
  },
  mounted(){
  },
  methods: {
  },
};
</script>