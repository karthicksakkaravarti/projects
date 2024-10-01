import Vue from 'vue'
import { i18n } from '@/plugins/i18n'
import '@/plugins/vue-composition-api'
import '@/styles/styles.scss'
import App from './App.vue'
import './plugins/acl'
import vuetify from './plugins/vuetify'
import router from './router'
import store from './store'

export const bus = new Vue()

// Using Debounce
import vueDebounce from 'vue-debounce'
Vue.use(vueDebounce)

Vue.config.productionTip = false

new Vue({
  router,
  store,
  i18n,
  vuetify,
  render: h => h(App),
}).$mount('#app')
