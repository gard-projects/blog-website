import { createStore } from 'vuex'

// Create a store instance.
const store = createStore({
    state() {
        return {
            user: null,
            loggedIn: false
        }
    },
    mutations: {
        setUser(state, user) {
            state.user = user
            state.loggedIn = true
        },
        logout(state) {
            state.user = null
            state.loggedIn = false
        }
    }
});

export default store;