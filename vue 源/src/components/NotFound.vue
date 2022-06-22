<template>
    <div class="err404">
        <h4>    您访问的页面不见了！</h4>
        <h5>
            <router-link to="../home" class="go-home">去首页</router-link>
        </h5>
    </div>
</template>

<script>
    export default {
        data() {
            return {}
        }
    }
</script>

<style>
    .err404 {
        width: 400px;
        margin: 100px auto;
        height: 400px;
        padding: 400px 0 0 420px;
        background-size: cover;
        background: url(../assets/404.gif) no-repeat 0 0;
    }

    .err404 h4 {
        font-size: 24px;
        color: #191919;
        padding-bottom: 16px;
        text-align: center;
    }

    .err404 .go-home {
        width: 200px;
        height: 38px;
        background: #1760ce;
        line-height: 38px;
        font-size: 16px;
        color: rgb(243, 87, 4);
        text-align: center;
        display: inline-block;
        border-radius: 2px
    }
</style>