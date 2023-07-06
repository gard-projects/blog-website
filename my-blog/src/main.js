import { createApp } from 'vue'
import App from './App.vue'
import Router from './router/router.js'
import Store from './store/store.js'

import { library } from '@fortawesome/fontawesome-svg-core'
import { faCaretDown, faMagnifyingGlass, faRightToBracket, faCircleUser, faEye, faEyeSlash } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(faCaretDown, faMagnifyingGlass, faRightToBracket, faCircleUser, faEye, faEyeSlash)

const app = createApp(App)
app.use(Router)
app.use(Store)
app.component('font-awesome-icon', FontAwesomeIcon)
app.mount('#app')
