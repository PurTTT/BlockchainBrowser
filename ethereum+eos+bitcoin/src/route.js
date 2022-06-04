import Vue from 'vue'
import Router from 'vue-router'
import etheInformation from "./components/etheInformation";
import etheTransaction from "./components/etheTransaction";
import etheBlocks from "./components/etheBlocks";
import etheInfo from "./components/etheInfo";
import eosInformation from "./components/eosInformation";
import eosTransaction from "./components/eosTransaction";
import eosBlocks from "./components/eosBlocks";
import eosInfo from "./components/eosInfo";
import bitInformation from "./components/bitInformation";
import bitTransaction from "./components/bitTransaction";
import bitBlocks from "./components/bitBlocks";
import bitInfo from "./components/bitInfo";

Vue.use(Router)

export default new Router({
	mode: 'history',
	base: process.env.BASE_URL,
	//routes中将url与组件映射起来
	routes: [
		{
			path: '/',
			redirect: '/etheInformation'
		},
		{
			path: '/etheInformation',
			component: etheInformation
		},
		{
			path: '/etheTransaction',
			component: etheTransaction
		},
		{
			path: '/etheBlocks',
			component: etheBlocks
		},
		{
			path: '/etheInfo/:heights',
			name: 'etheInfo',
			component: etheInfo,
			props: true
		},
		{
			path: '/bitInformation',
			component: bitInformation
		},
		{
			path: '/bitTransaction',
			component: bitTransaction
		},
		{
			path: '/bitBlocks',
			component: bitBlocks
		},
		{
			path: '/bitInfo/:heights',
			name: 'bitInfo',
			component: bitInfo,
			props: true
		},
		{
			path: '/eosInformation',
			component: eosInformation
		},
		{
			path: '/eosTransaction',
			component: eosTransaction
		},
		{
			path: '/eosBlocks',
			component: eosBlocks
		},
		{
			path: '/eosInfo/:heights',
			name: 'eosInfo',
			component: eosInfo,
			props: true
		}
	]
})
