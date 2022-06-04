import ElementUI from 'element-ui' //新添加
import 'element-ui/lib/theme-chalk/index.css' //新添加，避免后期打包样式不同，要放在import App from './App';之前

import Vue from 'vue'

import VueExtension from './plugins/vueExtension';
import App from './App.vue'
import router from './route.js'



Vue.use(ElementUI)   //新添加

Vue.use(VueExtension);

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router: router
}).$mount('#app')
