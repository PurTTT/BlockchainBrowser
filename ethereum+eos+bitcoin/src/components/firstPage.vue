<template>
  <div>
    <el-menu
      :default-active="activeIndex2"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
      background-color="#062f4f"
      text-color="#fff"
      active-text-color="#ffd04b">

      <el-menu-item><el-image :src="IconImgUrl" style="width: 50px; align-content: center"></el-image></el-menu-item>
      <el-menu-item><span style="font-size: 20px">区块链浏览器</span></el-menu-item>
      <el-submenu index="1">
        <template slot="title">以太坊</template>
        <router-link to="/etheTransaction"><el-menu-item index="1-1">交易信息</el-menu-item></router-link>
        <router-link to="/etheBlocks"><el-menu-item index="1-2">区块信息</el-menu-item></router-link>
        <router-link to="/etheInformation"><el-menu-item index="1-3">以太坊基本信息</el-menu-item></router-link>
      </el-submenu>
      <el-submenu index="2">
        <template slot="title">比特币</template>
        <router-link to="/bitTransaction"><el-menu-item index="2-1">交易信息</el-menu-item></router-link>
        <router-link to="/bitBlocks"><el-menu-item index="2-2">区块信息</el-menu-item></router-link>
        <router-link to="/bitInformation"><el-menu-item index="2-3">基本信息</el-menu-item></router-link>
<!--        <el-menu-item index="2-1">选项1</el-menu-item>-->
<!--        <el-menu-item index="2-2">选项2</el-menu-item>-->
<!--        <el-menu-item index="2-3">选项3</el-menu-item>-->
      </el-submenu>
      <el-submenu index="3">
        <template slot="title">eos</template>
        <router-link to="/eosTransaction"><el-menu-item index="3-1">交易信息</el-menu-item></router-link>
        <router-link to="/eosBlocks"><el-menu-item index="3-2">区块信息</el-menu-item></router-link>
        <router-link to="/eosInformation"><el-menu-item index="3-3">基本信息</el-menu-item></router-link>
      </el-submenu>
    </el-menu>
    <router-view></router-view>
  </div>
</template>


<script>
  import etheInformation from "./etheInformation";
  import etheTransaction from "./etheTransaction";
  import etheBlocks from "./etheBlocks";
  import eosInformation from "./eosInformation";
  import eosTransaction from "./eosTransaction";
  import eosBlocks from "./eosBlocks";
  import bitInformation from "./bitInformation";
  import bitTransaction from "./bitTransaction";
  import bitBlocks from "./bitBlocks";
  export default {
    name:'FirstPage',
    components:{
      etheInformation,
      etheTransaction,
      etheBlocks,
      bitInformation,
      bitTransaction,
      bitBlocks,   
      eosInformation,
      eosTransaction,
      eosBlocks
    },
    data() {
      return {
        activeIndex2: '1-3',
        IconImgUrl: require('../assets/blockchain.png')
      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>