<template>
  <div>
    <el-card style="margin-top: 20px">
      <div slot="header" class="clearfix">
        <span>区块信息</span>
      </div>
      <el-row><h3>{{this.block.block_num}}</h3></el-row>
      <el-row><span>{{this.block.id}}</span></el-row>
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
          var netUrl = "http://127.0.0.1:5000/block"; 
          var datas = { num:Number(this.$route.params.heights)}; 
          var myheaders = {"Content-Type": "application/json"};
//请求
        axios.post(netUrl,datas).then(resp=>{
        this.block=resp.data
        console.log(this.block.block_num);

//请求内处理结果
this.tableData = [{attr:'父区块哈希值', values:this.block.previous},
          {attr:'交易前缀树根', values:this.block.transaction_mroot},
          {attr:'矿工', values:this.block.producer},
          {attr:'时间戳', values:this.block.timestamp},
          {attr:'交易对象数量', values:this.block.transactions.length}]

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