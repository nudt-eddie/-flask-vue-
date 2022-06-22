<template>
  <div class="block">
    <el-timeline>
      <el-timeline-item
        v-for="(statuse) in this.$res_data_statuses.slice(0,10)"
        :key="statuse"
        :timestamp="statuse.created_at"
        placement="top"
      >
        <el-card>
          <h4 v-html='statuse.text'></h4>
          <p>点赞:{{ statuse.attitudes_count}}   评论:{{ statuse.comments_count }}</p>
        </el-card>
      </el-timeline-item>
    </el-timeline>

  </div>
</template>

<script>
export default {
  data() {
    return {
    };
  },
  mounted() {
  },
  methods:{
  }
};
</script>