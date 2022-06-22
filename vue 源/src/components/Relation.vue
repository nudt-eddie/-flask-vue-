<template>
  <div>
    <div ref="myPage" style="height: calc(100vh - 50px)">
      <SeeksRelationGraph
        ref="seeksRelationGraph"
        :options="graphOptions"
        :on-node-click="onNodeClick"
        :on-line-click="onLineClick"
      >
        <div
          slot="node"
          slot-scope="{ node }"
          @mouseover="showNodeTips(node, $event)"
          @mouseout="hideNodeTips(node, $event)"
        >
        <div class="c-my-node" v-bind:style="{backgroundImage:'url(' + node.data.url + ')',border:'#6cc0ff solid 3px'}"><div class="c-node-name" style="color: hsl(30, 100%, 50%);">{{node.data.name}}</div></div>

        </div>
      </SeeksRelationGraph>
    </div>
    <div
      v-if="isShowNodeTipsPanel"
      :style="{
        left: nodeMenuPanelPosition.x + 'px',
        top: nodeMenuPanelPosition.y + 'px',
      }"
      style="
        z-index: 999;
        padding: 10px;
        background-color: #ffffff;
        border: #eeeeee solid 1px;
        box-shadow: 0px 0px 8px #cccccc;
        position: absolute;
      "
    >
      <div
        style="
          line-height: 25px;
          padding-left: 10px;
          color: #888888;
          font-size: 12px;
        "
      >
        用户昵称：{{ currentNode.data.name }}
      </div>
      <div class="c-node-menu-item">地址:{{ currentNode.data.address }}</div>
      <div class="c-node-menu-item">关注:{{ currentNode.data.friends }}</div>
      <div class="c-node-menu-item">粉丝:{{ currentNode.data.fans }}</div>
      <div class="c-node-menu-item">微博:{{ currentNode.data.statuses }}</div>
      <!--div class="c-node-menu-item">链接:{{ currentNode.data.links }}</div-->
    </div>
  </div>
</template>

<script>
import SeeksRelationGraph from "relation-graph";
export default {
  name: "Demo",
  components: { SeeksRelationGraph },
  data() {
    return {
      isShowCodePanel: false,
      isShowNodeTipsPanel: false,
      nodeMenuPanelPosition: { x: 0, y: 0 },
      currentNode: {},
      graphOptions: {
        defaultNodeBorderWidth: 0,
        allowSwitchLineShape: true,
        defaultNodeColor: "rgba(255, 255, 255, 0)",
        allowSwitchJunctionPoint: true,
        defaultNodeWidth: 70,
        defaultNodeHeight: 70,
        defaultJunctionPoint: "border",
        'layouts': [
          {
            'label': '中心',
            'layoutName': 'tree',
            'layoutClassName': 'seeks-layout-center',
            'defaultJunctionPoint': 'border',
            'defaultNodeShape': 0,
            'defaultLineShape': 1,
            'from': 'left',
            'max_per_width': '300',
            'min_per_height': '40',
            /*
            'label': '自动布局',
            'layoutName': 'force',
            'layoutClassName': 'seeks-layout-force'     */
          },




        ],
        'defaultJunctionPoint': 'lr',
        // 这里可以参考"Graph 图谱"中的参数进行设置
      },
    };
  },
  mounted() {
    this.showSeeksGraph()
  },
  methods: {
    showSeeksGraph(query) {
      var __graph_json_data = {
        rootId: "1",
        nodes: [
          {
            id: "N1",
            expandHolderPosition:true,
            innerHTML: 
              '<div class="c-my-node">',
            data: {
               url: this.$res_data_user.avatar_url,
               name: this.$res_data_user.usname,
               address: this.$res_data_user.address,
               friends: this.$res_data_user.friends,
               fans: this.$res_data_user.fans,
               statuses: this.$res_data_user.counts,
               links: "https://weibo.com" + this.$res_data_user.profile_url
            }
          },
          {
            id: "N2",
            innerHTML:
              '<div class="c-my-node">',
            data: {
               url: this.$res_data_friends[1]["avatar_hd"],
               name: this.$res_data_friends[1]["name"],
               address: this.$res_data_friends[1]["location"],
               friends: this.$res_data_friends[1]["friends_count"],
               fans: this.$res_data_friends[1]["followers_count_str"],
               statuses: this.$res_data_friends[1]["statuses_count"],
               links:"https://weibo.com/u/" + this.$res_data_friends[1]["id"]
            }              
          },
          {
            id: "N3",
            innerHTML:
              '<div class="c-my-node">',
            data: {
               url: this.$res_data_friends[2]["avatar_hd"],
               name: this.$res_data_friends[2]["name"],
               address: this.$res_data_friends[2]["location"],
               friends: this.$res_data_friends[2]["friends_count"],
               fans: this.$res_data_friends[2]["followers_count_str"],
               statuses: this.$res_data_friends[2]["statuses_count"],
               links:"https://weibo.com/u/" + this.$res_data_friends[2]["id"]
            }                          
          },
          {
            id: "N4",
            innerHTML:
              '<div class="c-my-node">',
            data: {
               url: this.$res_data_friends[3]["avatar_hd"],
               name: this.$res_data_friends[3]["name"],
               address: this.$res_data_friends[3]["location"],
               friends: this.$res_data_friends[3]["friends_count"],
               fans: this.$res_data_friends[3]["followers_count_str"],
               statuses: this.$res_data_friends[3]["statuses_count"],
               links:"https://weibo.com/u/" + this.$res_data_friends[3]["id"]
            }              
          },
          {
            id: "N5",
            innerHTML:
              '<div class="c-my-node">',
            data: {
               url: this.$res_data_friends[4]["avatar_hd"],
               name: this.$res_data_friends[4]["name"],
               address: this.$res_data_friends[4]["location"],
               friends: this.$res_data_friends[4]["friends_count"],
               fans: this.$res_data_friends[4]["followers_count_str"],
               statuses: this.$res_data_friends[4]["statuses_count"],
               links: "https://weibo.com/u/" + this.$res_data_friends[4]["id"]
            }              
          },
          {
            id: "N6",
            innerHTML:
              '<div class="c-my-node">',
            data: {
               url: this.$res_data_friends[5]["avatar_hd"],
               name: this.$res_data_friends[5]["name"],
               address: this.$res_data_friends[5]["location"],
               friends: this.$res_data_friends[5]["friends_count"],
               fans: this.$res_data_friends[5]["followers_count_str"],
               statuses: this.$res_data_friends[5]["statuses_count"],
               links: "https://weibo.com/u/" + this.$res_data_friends[5]["id"]
            }              
          },
          {
            id: "N7",
            innerHTML:
              '<div class="c-my-node">',
            data: {
               url: this.$res_data_friends[6]["avatar_hd"],
               name: this.$res_data_friends[6]["name"],
               address: this.$res_data_friends[6]["location"],
               friends: this.$res_data_friends[6]["friends_count"],
               fans: this.$res_data_friends[6]["followers_count_str"],
               statuses: this.$res_data_friends[6]["statuses_count"],
               links: "https://weibo.com/u/" + this.$res_data_friends[6]["id"]
            }                          
          },
          {
            id: "N8",
            innerHTML:
              '<div class="c-my-node">',
            data: {
               url: this.$res_data_friends[7]["avatar_hd"],
               name: this.$res_data_friends[7]["name"],
               address: this.$res_data_friends[7]["location"],
               friends: this.$res_data_friends[7]["friends_count"],
               fans: this.$res_data_friends[7]["followers_count_str"],
               statuses: this.$res_data_friends[7]["statuses_count"],
               links: "https://weibo.com/u/" + this.$res_data_friends[7]["id"]
            }              
          },
          {
            id: "N9",
            innerHTML:
              '<div class="c-my-node">',
            data: {
               url: this.$res_data_friends[8]["avatar_hd"],
               name: this.$res_data_friends[8]["name"],
               address: this.$res_data_friends[8]["location"],
               friends: this.$res_data_friends[8]["friends_count"],
               fans: this.$res_data_friends[8]["followers_count_str"],
               statuses: this.$res_data_friends[8]["statuses_count"],
               links: "https://weibo.com/u/" + this.$res_data_friends[8]["id"]
            }              
          },
          {
            id: "N10",
            innerHTML:
              '<div class="c-my-node">',
            data: {
               url: this.$res_data_friends[9]["avatar_hd"],
               name: this.$res_data_friends[9]["name"],
               address: this.$res_data_friends[9]["location"],
               friends: this.$res_data_friends[9]["friends_count"],
               fans: this.$res_data_friends[9]["followers_count_str"],
               statuses: this.$res_data_friends[9]["statuses_count"],
               links:"https://weibo.com/u/" + this.$res_data_friends[9]["id"]
            }              
          },
          {
            id: "N11",
            innerHTML:
              '<div class="c-my-node">',
            data: {
               url: this.$res_data_friends[10]["avatar_hd"],
               name: this.$res_data_friends[10]["name"],
               address: this.$res_data_friends[10]["location"],
               friends: this.$res_data_friends[10]["friends_count"],
               fans: this.$res_data_friends[10]["followers_count_str"],
               statuses: this.$res_data_friends[10]["statuses_count"],
               links: "https://weibo.com/u/" + this.$res_data_friends[10]["id"]
            }              
          },
          {
            id: "N12",
            innerHTML:
              '<div class="c-my-node">',
            data: {
               url: this.$res_data_fans[1]["avatar_hd"],
               name: this.$res_data_fans[1]["name"],
               address: this.$res_data_fans[1]["location"],
               friends: this.$res_data_fans[1]["friends_count"],
               fans: this.$res_data_fans[1]["followers_count_str"],
               statuses: this.$res_data_fans[1]["statuses_count"],
               links: "https://weibo.com/u/" + this.$res_data_fans[1]["id"]
            }              
          },
          {
            id: "N13",
            innerHTML:
              '<div class="c-my-node">',
            data: {
               url: this.$res_data_fans[2]["avatar_hd"],
               name: this.$res_data_fans[2]["name"],
               address: this.$res_data_fans[2]["location"],
               friends: this.$res_data_fans[2]["friends_count"],
               fans: this.$res_data_fans[2]["followers_count_str"],
               statuses: this.$res_data_fans[2]["statuses_count"],
               links: "https://weibo.com/u/" + this.$res_data_fans[2]["id"]
            }                          
          },
          {
            id: "N14",
            innerHTML:
              '<div class="c-my-node">',
            data: {
               url: this.$res_data_fans[3]["avatar_hd"],
               name: this.$res_data_fans[3]["name"],
               address: this.$res_data_fans[3]["location"],
               friends: this.$res_data_fans[3]["friends_count"],
               fans: this.$res_data_fans[3]["followers_count_str"],
               statuses: this.$res_data_fans[3]["statuses_count"],
               links: "https://weibo.com/u/" + this.$res_data_fans[3]["id"]
            }              
          },
          {
            id: "N15",
            innerHTML:
              '<div class="c-my-node">',
            data: {
               url: this.$res_data_fans[4]["avatar_hd"],
               name: this.$res_data_fans[4]["name"],
               address: this.$res_data_fans[4]["location"],
               friends: this.$res_data_fans[4]["friends_count"],
               fans: this.$res_data_fans[4]["followers_count_str"],
               statuses: this.$res_data_fans[4]["statuses_count"],
               links: "https://weibo.com/u/" + this.$res_data_fans[4]["id"]
            }              
          },
          {
            id: "N16",
            innerHTML:
              '<div class="c-my-node">',
            data: {
               url: this.$res_data_fans[5]["avatar_hd"],
               name: this.$res_data_fans[5]["name"],
               address: this.$res_data_fans[5]["location"],
               friends: this.$res_data_fans[5]["friends_count"],
               fans: this.$res_data_fans[5]["followers_count_str"],
               statuses: this.$res_data_fans[5]["statuses_count"],
               links: "https://weibo.com/u/" + this.$res_data_fans[5]["id"]
            }              
          },
          {
            id: "N17",
            innerHTML:
              '<div class="c-my-node">',
            data: {
               url: this.$res_data_fans[6]["avatar_hd"],
               name: this.$res_data_fans[6]["name"],
               address: this.$res_data_fans[6]["location"],
               friends: this.$res_data_fans[6]["friends_count"],
               fans: this.$res_data_fans[6]["followers_count_str"],
               statuses: this.$res_data_fans[6]["statuses_count"],
               links: "https://weibo.com/u/" + this.$res_data_fans[6]["id"]
            }                          
          },
          {
            id: "N18",
            innerHTML:
              '<div class="c-my-node">',
            data: {
               url: this.$res_data_fans[7]["avatar_hd"],
               name: this.$res_data_fans[7]["name"],
               address: this.$res_data_fans[7]["location"],
               friends: this.$res_data_fans[7]["friends_count"],
               fans: this.$res_data_fans[7]["followers_count_str"],
               statuses: this.$res_data_fans[7]["statuses_count"],
               links: "https://weibo.com/u/" + this.$res_data_fans[7]["id"]
            }              
          },
          {
            id: "N19",
            innerHTML:
              '<div class="c-my-node">',
            data: {
               url: this.$res_data_fans[8]["avatar_hd"],
               name: this.$res_data_fans[8]["name"],
               address: this.$res_data_fans[8]["location"],
               friends: this.$res_data_fans[8]["friends_count"],
               fans: this.$res_data_fans[8]["followers_count_str"],
               statuses: this.$res_data_fans[8]["statuses_count"],
               links: "https://weibo.com/u/" + this.$res_data_fans[8]["id"]
            }              
          },
          {
            id: "N20",
            innerHTML:
              '<div class="c-my-node">',
            data: {
               url: this.$res_data_fans[9]["avatar_hd"],
               name: this.$res_data_fans[9]["name"],
               address: this.$res_data_fans[9]["location"],
               friends: this.$res_data_fans[9]["friends_count"],
               fans: this.$res_data_fans[9]["followers_count_str"],
               statuses: this.$res_data_fans[9]["statuses_count"],
               links: "https://weibo.com/u/" + this.$res_data_fans[9]["id"]
            }              
          },
          {
            id: "N21",
            innerHTML:
              '<div class="c-my-node">',
            data: {
               url: this.$res_data_fans[10]["avatar_hd"],
               name: this.$res_data_fans[10]["name"],
               address: this.$res_data_fans[10]["location"],
               friends: this.$res_data_fans[10]["friends_count"],
               fans: this.$res_data_fans[10]["followers_count_str"],
               statuses: this.$res_data_fans[10]["statuses_count"],
               links: "https://weibo.com/u/" + this.$res_data_fans[10]["id"]
            }              
          },
        ],
        links: [
          {
            from: "N1",
            to: "N2",
            text: "关注",
            color: "#20B2AA",
            fontColor: "#20B2AA",
          },
          {
            from: "N1",
            to: "N3",
            text: "关注",
            color: "#20B2AA",
            fontColor: "#20B2AA",
          },
          {
            from: "N1",
            to: "N4",
            text: "关注",
            color: "#20B2AA",
            fontColor: "#20B2AA",
          },
          {
            from: "N1",
            to: "N5",
            text: "关注",
            color: "#20B2AA",
            fontColor: "#20B2AA",
          },
          {
            from: "N1",
            to: "N6",
            text: "关注",
            color: "#20B2AA",
            fontColor: "#20B2AA",
          },
          {
            from: "N1",
            to: "N7",
            text: "关注",
            color: "#20B2AA",
            fontColor: "#20B2AA",
          },
          {
            from: "N1",
            to: "N8",
            text: "关注",
            color: "#20B2AA",
            fontColor: "#20B2AA",
          },
          {
            from: "N1",
            to: "N9",
            text: "关注",
            color: "#20B2AA",
            fontColor: "#20B2AA",
          },
          {
            from: "N1",
            to: "N10",
            text: "关注",
            color: "#20B2AA",
            fontColor: "#20B2AA",
          },
          {
            from: "N1",
            to: "N11",
            text: "关注",
            color: "#20B2AA",
            fontColor: "#20B2AA",
          },
          {
            from: "N12",
            to: "N1",
            text: "关注",
            color: "#2E8B57",
            fontColor: "#2E8B57",
          },
          {
            from: "N13",
            to: "N1",
            text: "关注",
            color: "#2E8B57",
            fontColor: "#2E8B57",
          },
          {
            from: "N14",
            to: "N1",
            text: "关注",
            color: "#2E8B57",
            fontColor: "#2E8B57",
          },
          {
            from: "N15",
            to: "N1",
            text: "关注",
            color: "#2E8B57",
            fontColor: "#2E8B57",
          },
          {
            from: "N16",
            to: "N1",
            text: "关注",
            color: "#2E8B57",
            fontColor: "#2E8B57",
          },
          {
            from: "N17",
            to: "N1",
            text: "关注",
            color: "#2E8B57",
            fontColor: "#2E8B57",
          },
          {
            from: "N18",
            to: "N1",
            text: "关注",
            color: "#2E8B57",
            fontColor: "#2E8B57",
          },
          {
            from: "N19",
            to: "N1",
            text: "关注",
            color: "#2E8B57",
            fontColor: "#2E8B57",
          },
          {
            from: "N20",
            to: "N1",
            text: "关注",
            color: "#2E8B57",
            fontColor: "#2E8B57",
          },
          {
            from: "N21",
            to: "N1",
            text: "关注",
            color: "#2E8B57",
            fontColor: "#2E8B57",
          },
        ],
      };
      console.log(__graph_json_data.nodes[0]);
      console.log(__graph_json_data)
      this.$refs.seeksRelationGraph.setJsonData(
        __graph_json_data,
        (seeksRGGraph) => {
          // 这些写上当图谱初始化完成后需要执行的代码
        }
      );
    },

    onNodeClick(nodeObject, $event) {
      console.log("onNodeClick:", nodeObject);
      this.$notify({
        title: nodeObject.data.name,
        message: nodeObject.data.links
      })
    },
    onLineClick(lineObject, $event) {
      console.log("onLineClick:", lineObject);
    },
    showNodeTips(nodeObject, $event) {
      this.currentNode = nodeObject;
      var _base_position = this.$refs.myPage.getBoundingClientRect();
      console.log("showNodeMenus:", $event, _base_position);
      this.isShowNodeTipsPanel = true;
      this.nodeMenuPanelPosition.x = $event.clientX - _base_position.x + 10;
      this.nodeMenuPanelPosition.y = $event.clientY - _base_position.y + 10;
    },
    hideNodeTips(nodeObject, $event) {
      this.isShowNodeTipsPanel = false;
    },
  },
};
</script>


<style scoped>
.c-node-menu-item {
  line-height: 30px;
  padding-left: 10px;
  cursor: pointer;
  color: #444444;
  font-size: 14px;
  border-top: #efefef solid 1px;
}
.c-node-menu-item:hover {
  background-color: rgba(66, 187, 66, 0.2);
}
.c-my-node {
  background-position: center center;
  background-size: 100%;
  border: #281692 solid 100px;
  height: 80px;
  width: 80px;
  border-radius: 100px;
}
.c-node-name {
  width: 160px;
  margin-left: -40px;
  text-align: center;
  margin-top: 85px;
}
</style>