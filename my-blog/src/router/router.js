import store from '../store/store.js'

import { createRouter, createWebHashHistory } from 'vue-router'
import About from '../components/About.vue'
import Trending from '../components/Trending.vue'
import Plans from '../components/Plans.vue'
import Login from '../components/UserLogin.vue'
import Signup from '../components/UserSignup.vue'

// Routes
const routes = [
    { path: '/about', component: About },
    { path: '/trending', component: Trending },
    { path: '/plans', component: Plans, meta: { isAuthenticated: true } },
    { path: '/login', component: Login },
    { path: '/signup', component: Signup }
];

// Create router instance
const router = createRouter({
    history: createWebHashHistory(),
    routes
})

// Handle user authentication
router.beforeEach((to) => {
   if(to.meta.isAuthenticated && to.name !== 'login') {
       if(!store.state.loggedIn) {
           router.push('/login')
       }
   }
}); 

export default router