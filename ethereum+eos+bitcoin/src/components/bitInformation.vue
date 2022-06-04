<template>
  <div>
    <el-container>
      <el-header><h3>{{message}}</h3></el-header>
      <el-main>
        <el-row>
        <el-col :span="12" style="float:left;">
            <el-input
              type="text"
              v-model="heights"
              placeholder="127168196s"
              style="cursor: pointer;"
              @keyup.enter.native="search()"
            >
            <el-button type="primary" slot="append" icon="el-icon-search" @click="search()"></el-button>
            </el-input>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "bitInformation",
  data: function(){
			return {
        heights: 739129,
        message: '区块信息搜索'
      }
		},
  methods:{
      search(){
        var re = /^[0-9]+.?[0-9]*/;//判断字符串是否为数字//判断正整数/[1−9]+[0−9]∗]∗/
      　if(!re.test(this.heights)) {
      　　　　alert("请输入数字!");
　　    }
        else {
           this.$router.push({name: 'bitInfo', params: {heights: this.heights}})
        }
      }
    }
}
</script>

<style>
  .el-input__inner{
    border-color: #062f4f;
    border-width: 3px;
    border-radius: 6px;
  }
  /deep/el-input::-webkit-input-placeholder{
    color: #062f4f;
  }
  .el-input-group__append button.el-button{
          background-color: #062f4f;
          border-color: #062f4f;
  }
  .el-input-group__append{
    background-color: #062f4f;
    border: #062f4f;
    color: #f2f2f2;
  }
</style>