<template>
  <div>
    <el-card style="margin-top: 20px">
      <div slot="header" class="clearfix">
        <span>区块信息</span>
      </div>
      <el-row><h3>{{this.block.number}}</h3></el-row>
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
    name: "etheInfo",
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
        if (typeof window.web3 !== 'undefined') {
          window.web3 = new Web3(window.web3.currentProvider);
        } else {
          const ethNodeUrl = new Web3.providers.HttpProvider('http://localhost:8545'); // TODO: remote URL
          window.web3 = new Web3(ethNodeUrl);
          console.log(window.web3);
        }
        const { eth } = window.web3;
        const block = await eth.getBlock(this.$route.params.heights);
        block.timestamp = this.$filters.difference(block.timestamp);
        console.log(block.timestamp)
        this.block = block
        this.tableData = [{attr:'父区块哈希值', values:block.parentHash},
          {attr:'工作量证明哈希值', values:block.nonce},
          {attr:'叔区块哈希值', values:block.sha3Uncles},
          {attr:'交易前缀树根', values:block.transactionsRoot},
          {attr:'最终状态前缀树根', values:block.stateRoot},
          {attr:'矿工', values:block.miner},
          {attr:'难度', values:block.difficulty},
          {attr:'当前总难度', values:block.totalDifficulty},
          {attr:'块大小', values:block.size},
          {attr:'总gas', values:block.gasLimit},
          {attr:'已用gas', values:block.gasUsed},
          {attr:'时间戳', values:block.timestamp},
          {attr:'交易对象数量', values:block.transactions.length}]
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