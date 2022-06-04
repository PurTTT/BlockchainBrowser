<template>
  <div>
    <el-container>
      <el-main>
        <el-card>
          <h3  v-text="title"></h3>
          <div class="table transactions">
          <div class="table-header">
            <div class="table-row">
                <div class="table-column">交易哈希</div>
                <div class="table-column">区块哈希</div>
                <div class="table-column">区块高度</div>
                <div class="table-column">时间戳</div>
                <div class="table-column">从</div>
                <div class="table-column">到</div>
                <div class="table-column">价值</div>
                <div class="table-column">Gas限额</div>
                <div class="table-column">Gas价格</div>
                <div class="table-column">工作量证明哈希值</div>
                <div class="table-column">交易ID</div>
                <!-- <div class="table-column">input</div>
                <div class="table-column">r</div>
                <div class="table-column">s</div>
                <div class="table-column">v</div> -->
            </div>
          </div>
        <div v-if="loading || txs.length" class="table-body" :class="`${loading ? 'table-body-loading' : ''}`" >
          <div class="table-row" v-for="(tx,i) in txs" :key="`tx-${i}`">
            <div class="table-column" v-text="tx.hash"></div>
            <div class="table-column" v-text="tx.blockHash"></div>
            <div class="table-column" v-text="tx.blockNumber"></div>
            <div class="table-column" v-text="tx.timestamp"></div>
            <div class="table-column" v-text="tx.from"></div>
            <div class="table-column" v-text="tx.to"></div>
            <div class="table-column" v-text="tx.value"></div>
            <div class="table-column" v-text="tx.gas"></div>
            <div class="table-column" v-text="tx.gasPrice"></div>
            <div class="table-column" v-text="tx.nonce"></div>
            <div class="table-column" v-text="tx.transactionIndex"></div>
            <!-- <div class="table-column" v-text="tx.input"></div>
            <div class="table-column" v-text="tx.r"></div>
            <div class="table-column" v-text="tx.s"></div>
            <div class="table-column" v-text="tx.v"></div> -->
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
      title: '以太坊最新交易',
      name:'etheTransaction',
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