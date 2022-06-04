<template>
  <div>
    <el-container>
      <el-main>
        <el-card>
          <h3  v-text="title"></h3>
          <div class="table blocks">
      <div class="table-header">
        <div class="table-row">
          <div class="table-column">区块高度</div>
          <div class="table-column">时间戳</div>
          <div class="table-column">交易对象数量</div>
          <div class="table-column">矿工</div>
          <div class="table-column">哈希</div>
          <div class="table-column">父区块哈希</div>
          <!-- <div class="table-column">Uncles</div>
          <div class="table-column">difficulty</div>
          <div class="table-column">extraData</div>
          <div class="table-column">logsBloom</div>
          <div class="table-column">stateRoot</div>
          <div class="table-column">totalDifficulty</div>
          <div class="table-column">transactionsRoot</div> -->
        </div>
      </div>
      <div v-if="loading || blocks.length" class="table-body" :class="`${loading ? 'table-body-loading' : ''}`">
        <div class="table-row" v-for="(block,i) in blocks" :key="`block-${i}`">
          <div class="table-column" v-text="block.block_num"></div>
          <div class="table-column" v-text="block.timestamp"></div>
          <div class="table-column" v-text="block.txn"></div>
          <div class="table-column" v-text="block.producer"></div>
          <div class="table-column" v-text="block.id"></div>
          <div class="table-column" v-text="block.previous"></div>
          <!-- <div class="table-column" v-text="block.sha3Uncles"></div>
          <div class="table-column" v-text="block.difficulty"></div>
          <div class="table-column" v-text="block.extraData"></div>
          <div class="table-column" v-text="block.logsBloom"></div>
          <div class="table-column" v-text="block.stateRoot"></div>
          <div class="table-column" v-text="block.totalDifficulty"></div>
          <div class="table-column" v-text="block.transactionsRoot"></div> -->
        </div>
      </div>
      <div v-else class="table-body-nodata">No data</div>
    </div>
        </el-card>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import Web3 from 'web3';

export default {
  data() {
    return {
      title: 'EOS最新区块',
      name:'eosBlocks',
      blocks: [],
      txs: [],
      timmer: null,
      loading: true
    };
  },
  created() {
    if (typeof window.web3 !== 'undefined') {
      window.web3 = new Web3(window.web3.currentProvider);
    } else {
      const ethNodeUrl = new Web3.providers.HttpProvider('http://localhost:8545'); // TODO: remote URL
      window.web3 = new Web3(ethNodeUrl);
      console.log(window.web3);
    }


    this.refreshData();
    this.timmer = setInterval(() => {
      this.refreshData();
    }, 60000);
  },
  methods: {
    refreshData(){
      try {
        this.printBlocksAndTxs();
      } catch (err) {
        console.log(err);
      }
    },

    async getBlocksAndTxs() {
//存blocknum
      var blockNumber = 0;
      var blocks = [];
      var block ={'timestamp':0,'block.txn':0};
      let txs = [];

//axios的定义
      const axios = require('axios');
//定义变量
      var netUrl = "http://127.0.0.1:5000/info";
      var myheaders = {"Content-Type": "application/json"};
//请求
        await axios.post(netUrl).then(resp=>{
            block=resp.data
            blockNumber = resp.data.num;
            console.log(resp.data.num);
            console.log(blockNumber);
            console.log("已获得数字");
        }).catch(resp=>{
            console.log('my miss');
        });
//axios请求结束

      for (let i = 1; i <= 15; i++) {
          console.log('???');
        //const block = await eth.getBlock(blockNumber-i);
//定义变量
          var netUrl = "http://127.0.0.1:5000/block"; 
          var myheaders = {"Content-Type": "application/json"};
//请求
        await axios.post(netUrl,{ num:blockNumber-i}).then(resp=>{
        block=resp.data
        console.log('lets go');
        console.log(blocks);

//请求内处理结果

//请求处理结果完成
        }).catch(resp=>{
        console.log('my miss');
        })
//axios请求结束

        block.timestamp = block.timestamp;
        block.txn = block.transactions.length;
        blocks.push(block);
        txs = txs.concat(block.transactions);
      }
//for end
        console.log(txs);
        console.log('blocks');
        console.log(blocks);
        blocks.push(block);
      return {
        blocks,txs
      };
    },

    async printBlocksAndTxs() {
      const { eth } = window.web3;
      const result = await this.getBlocksAndTxs();

      const txs = result.txs;
      const handledTxs = [];

      let len = 0;
      if (len) {
        for (let i = 1; i < 15; i++) {
          const handledTx = await eth.getTransaction(txs[len-i]);

          Object.keys(result.blocks).map(key => {
            if(result.blocks[key].number === handledTx.blockNumber){
              handledTx.timestamp = result.blocks[key].timestamp;
            }
          })
          handledTxs.push(handledTx);
        }
      }

      this.loading = false;
      this.blocks = result.blocks;
      this.txs = handledTxs;
    }
  },
  beforeDestroy(){
    this.timmer && (this.timmer = null);
  }
};
</script>

<style lang="less" scoped>
.subtitle {
  text-align: left;
}

@table-border: 1px solid #ddd;

.table {
  border-top: @table-border;
}
.table-header {
  .table-row {
    background-color: #f9f9f9;
    &:hover {
      background-color: #f9f9f9;
    }
  }
}
.table-body-loading{
  background: url("../assets/loading.gif") center center no-repeat;
  background-size: 20px 20px;
  height: 60px;
  overflow: hidden;
}
.table-body-nodata{
  text-align: center;
  padding: 30px;
}
.table-row {
  display: flex;
  border-bottom: @table-border;
  padding: 12px;
  &:hover {
    background-color: #f2f2f2;
  }
}
.table-column {
  flex: 1;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>