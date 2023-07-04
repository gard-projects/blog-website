import { createRouter, createWebHashHistory } from 'vue-router'
import About from '../components/About.vue'
import Trending from '../components/Trending.vue'
import Plans from '../components/Plans.vue'
import Login from '../components/UserLogin.vue'
import Signup from '../components/UserSignup.vue'
import App from '../App.vue'

// Routes
const routes = [
    { path: '/', component: App},
    { path: '/about', component: About },
    { path: '/trending', component: Trending },
    { path: '/plans', component: Plans },
    { path: '/login', component: Login },
    { path: '/signup', component: Signup }
];

// Create router instance
const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router