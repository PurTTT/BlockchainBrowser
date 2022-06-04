<template>
  <div>
    <el-card style="margin-top: 20px">
      <div slot="header" class="clearfix">
        <span>区块信息</span>
      </div>
      <el-row><h3>{{this.block.height}}</h3></el-row>
      <el-row><span>{{this.block.hash}}</span></el-row>
      <el-table
            :data="tableData"
            style="width: 100%">
            <el-table-column
              prop="attr"
              label=""
              width="200px">
            </el-table-column>
            <el-table-column
              prop="values"
              label="">
            </el-table-column>
      </el-table>
    </el-card>
  </div>
</template>

<script>


  import Web3 from 'web3';
  export default {
    name: "eosInfo",
    data: function(){
        return {
          block:null,
          tableData: []
        }
      },
    mounted: function () {
      try {
        this.getBlock();
      } catch (err) {
        console.log(err);
      }
    },
    methods: {
     

async getBlock(){
//axios的定义
const axios = require('axios');
//定义变量
          var netUrl = "http://127.0.0.1:5000/bitBlock"; 
          var datas = { num:Number(this.$route.params.heights)}; 
          var myheaders = {"Content-Type": "application/json"};
//请求
        axios.post(netUrl,datas).then(resp=>{
        this.block=resp.data.blocks[0]
        var modifiedTime = new Date(this.block.time * 1000)
        this.modifiedTimeStr = String(modifiedTime)
        console.log(this.block);

//请求内处理结果
this.tableData = [{attr:'前序区块哈希', values:this.block.prev_block},
          {attr:'默克尔树根哈希', values:this.block.mrkl_root},
          // {attr:'矿工', values:this.block.producer},
          {attr:'时间戳', values:this.modifiedTimeStr},
          {attr:'交易数量', values:this.block.n_tx},
          {attr:'区块字节数', values:this.block.size},
          {attr:'区块索引', values:this.block.block_index}]

//请求处理结果完成
        }).catch(resp=>{
        console.log('my miss');
        })
//axios请求结束



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