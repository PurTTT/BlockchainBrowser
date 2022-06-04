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
          <div class="table-column">首笔交易时间</div>
          <div class="table-column">交易对象数量</div>
          <div class="table-column">矿工</div>
          <div class="table-column">Gas使用量</div>
          <div class="table-column">Gas限额</div>
          <div class="table-column">哈希</div>
          <div class="table-column">随机值</div>
          <div class="table-column">工作量证明哈希值</div>
          <div class="table-column">父区块哈希</div>
          <div class="table-column">收据</div>
          <div class="table-column">区块大小</div>
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
          <div class="table-column" v-text="block.number"></div>
          <div class="table-column" v-text="block.timestamp"></div>
          <div class="table-column" v-text="block.txn"></div>
          <div class="table-column" v-text="block.miner"></div>
          <div class="table-column" v-text="block.gasUsed"></div>
          <div class="table-column" v-text="block.gasLimit"></div>
          <div class="table-column" v-text="block.hash"></div>
          <div class="table-column" v-text="block.mixHash"></div>
          <div class="table-column" v-text="block.nonce"></div>
          <div class="table-column" v-text="block.parentHash"></div>
          <div class="table-column" v-text="block.receiptsRoot"></div>
          <div class="table-column" v-text="block.size"></div>
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
      title: '以太坊最新区块',
      name:'etheBlocks',
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

    // const { eth } = window.web3;

    // eth.getBlockNumber().then(function(resolve) {
    //   console.log(`getBlockNumber:${resolve}`);
    // });

    // eth.getAccounts().then(function(resolve) {
    //   console.log(`getAccounts:${resolve}`);
    // });

    // eth
    //   .getTransactionCount('0x7900681181e87B926A279769538f5325088eAdc1')
    //   .then(function(resolve) {
    //     console.log(`getTransactionCount:${resolve}`);
    //   });

    // eth.getCoinbase().then(function(resolve) {
    //   console.log(`getCoinbase:${resolve}`);
    // });

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
      const { eth } = window.web3;
      const blockNumber = await eth.getBlockNumber();
      const blocks = [];
      let txs = [];

      for (let i = 1; i <= 15; i++) {
        const block = await eth.getBlock(blockNumber-i);

        block.timestamp = this.$filters.difference(block.timestamp);
        block.txn = block.transactions.length;

        blocks.push(block);
        txs = txs.concat(block.transactions);
      }

      return {
        blocks,
        txs
      };
    },

    async printBlocksAndTxs() {
      const { eth } = window.web3;
      const result = await this.getBlocksAndTxs();

      const txs = result.txs;
      const handledTxs = [];

      let len = result.txs.length;
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