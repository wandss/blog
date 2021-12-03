import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import {BootstrapVue, IconsPlugin} from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import marked from 'marked'

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

/*
Vue.mixin({
    methods: {
        marked: function(input) {
            return marked(input);
        }
    }
});
*/

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
