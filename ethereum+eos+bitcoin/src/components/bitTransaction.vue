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
                <!-- <div class="table-column">区块哈希</div> -->
                <!-- <div class="table-column">区块高度</div> -->
                <div class="table-column">时间戳</div>
                <div class="table-column">交易输入数量</div>
                <div class="table-column">交易输出数量</div>
                <div class="table-column">交易字节数</div>
                <div class="table-column">费用</div>
                <div class="table-column">交易索引</div>
                <!-- <div class="table-column">交易状态</div> -->
                <!-- <div class="table-column">action</div> -->
                <!-- <div class="table-column">in put</div>
                <div class="table-column">r</div>
                <div class="table-column">s</div>
                <div class="table-column">v</div> -->
            </div>
          </div>
        <div v-if="loading || txs.length" class="table-body" :class="`${loading ? 'table-body-loading' : ''}`" >
          <div class="table-row" v-for="(tx,i) in txs" :key="`tx-${i}`">
            <div class="table-column" v-text="tx.hash"></div>
            <!-- <div class="table-column" v-text="tx.blockHash"></div> -->
            <!-- <div class="table-column" v-text="tx.blockNumber"></div> -->
            <div class="table-column" v-text="new Date(tx.time * 1000)"></div>
            <div class="table-column" v-text="tx.vin_sz"></div>
            <div class="table-column" v-text="tx.vout_sz"></div>
            <div class="table-column" v-text="tx.size"></div>
            <div class="table-column" v-text="tx.fee"></div>
            <div class="table-column" v-text="tx.tx_index"></div>
            <!-- <div class="table-column" v-text="tx.status"></div> -->
            <!-- <div class="table-column" v-text="tx.action"></div> -->
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
      title: '比特币最新未确认交易',
      name:'etheTransaction',
      blocks: [],
      txs: [],
      timmer: null,
      loading: true
    };
  },
  created() {

    this.refreshData();
    this.timmer = setInterval(() => {
      this.refreshData();
    }, 1000000);
  },
  methods: {
    refreshData(){
      try {
        this.printBlocksAndTxs();
      } catch (err) {
        console.log(err);
      }
    },


    async printBlocksAndTxs() {
     var mytxs
//axios的定义
      const axios = require('axios');
      
      var netUrl = "http://127.0.0.1:5000/bitTx"; 
      var myheaders = {"Content-Type": "application/json"};
      await axios.post(netUrl).then(resp=>{
        mytxs=resp.data;
        console.log('lets go');

        console.log(mytxs);

//请求内处理结果

//请求处理结果完成
        }).catch(resp=>{
        console.log(resp);
        });
//axios请求结束


      const myresult = mytxs.txs;
        console.log(myresult);
    //   const handledTxs = [];
    //  var relen = myresult.length;
    //   let txlen = 0;
    //   for (let i = 0; i < relen; i++) {txlen += myresult[i].transactions.length;}
	//    console.log("relen",relen,'txlen',txlen);

    //   let len = txlen;
    //   if (len) {
        // for (let i = 0; i < relen; i++) {
//处理格式  
	//    var tlen = myresult[i].transactions.length;
	//    console.log("处理",tlen);
        //    for (let j = 0; j < tlen; j++) {
        //    	var handledTx = {
		// 	//与块有关
		// 	'blockHash':myresult[i].id,
		// 	'blockNumber':myresult[i].block_num,
		// 	'timestamp':myresult[i].timestamp,
		// 	//不到trx
		// 	'net_usage':myresult[i].transactions[j].net_usage_words,
		// 	'cpu_usage':myresult[i].transactions[j].cpu_usage_us,
		// 	'status':myresult[i].transactions[j].status,
		// 	//trx内
  		// 	'hash':myresult[i].transactions[j].trx.id,
		// 	//transaction.action[0]内
		// 	'user':myresult[i].transactions[j].trx.transaction.actions[0].account,
		// 	'action':myresult[i].transactions[j].trx.transaction.actions[0].name,
		// 	//data内
		// 	'supplier':myresult[i].transactions[j].trx.transaction.actions[0].data.supplier,
		// 	'value':myresult[i].transactions[j].trx.transaction.actions[0].data.value
		// };
		// handledTxs.push(handledTx);
		// console.log(handledTx)
		//一条交易格式处理完成
	    // }
        // }
    //   }

      this.loading = false;
      this.txs = myresult;
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