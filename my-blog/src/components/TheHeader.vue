<script>
    import { mapState } from 'vuex'
    export default {
        name: 'TheHeader',
        data() {
            return {
                title: 'Thought Vault',
                description: 'A place to store your thoughts',
                isVisible: null
            }
        },

        methods: {
            loginUser() {
               return this.$router.push('/login');
            },
            openOptionsMenu() {
                this.isVisible = !this.isVisible;
            },
            closeOptionsMenu() {
                this.isVisible = false;
            }
        },

        computed: mapState({
            // mapState allows us to map our computed property to the state property of the Vuex store object
            isUserLoggedIn: state => state.loggedIn,
            getProfileImage: state => state.user.profile_image
        }),

    }
</script>

<template>
    <header>
        <div class="header-part__logo">
            <h1>{{ title }}</h1>
        </div>
        <nav class="header-part__nav">
            <ul class="header-nav">
                <div class="header-nav__item">
                    <li><router-link to="/">Home</router-link></li>
                    <font-awesome-icon icon="caret-down" />
                </div>
                <div class="header-nav__item">
                    <li><router-link to="/plans">Plans</router-link></li>
                    <font-awesome-icon icon="caret-down" />
                </div>
                <div class="header-nav__item">
                    <li><router-link to="/trending">Trending</router-link></li>
                    <font-awesome-icon icon="caret-down" />
                </div>
                <div class="header-nav__item">
                    <li><router-link to="/about">About</router-link></li>
                    <font-awesome-icon icon="caret-down" />
                </div>      
            </ul>
        </nav>
        <div class="header-part-func">
            <div class="search-container">
                <input type="text" placeholder="Search..." class="search-container__input">
                <font-awesome-icon icon="magnifying-glass" class="search-container__icon"/>
            </div>
            <div>
                <font-awesome-icon
                v-if="!isUserLoggedIn" 
                icon="circle-user" 
                class="header-part-func__user" 
                @click="loginUser"></font-awesome-icon>

                <img class="profile-image" 
                v-else :src="getProfileImage" 
                alt="No logo" width="40" height="40"
                @click="openOptionsMenu">
            </div>
            
        </div>
        <div class="options-menu" 
        v-if="isUserLoggedIn && (isVisible !== null)" 
        :class="isVisible === null ? '' : ( isVisible ? 'slide-out': 'slide-in')">
            <ul class="options-menu-list">
                <li class="options-menu-list__item">Profile</li>
                <li class="options-menu-list__item">Settings</li>
                <li class="options-menu-list__item">Support</li>
                <li class="options-menu-list__item">Logout</li>
            </ul>
            <font-awesome-icon icon="xmark" class="close-options-menu" @click="closeOptionsMenu"/>
        </div>
    </header>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Raleway&display=swap');
    header {
        position: relative;
        display: flex;
        align-items: center;
        column-gap: 20px;
        padding: 5px;
        background-color: #5ABCB9;
        color: white;
        font-weight: bold;
    }

    .header-part__logo * {
        font-family: 'Raleway', sans-serif;
        font-size: 30px;
    }   

    .header-nav {
        list-style: none;
        display: flex;
        column-gap: 40px;
        align-items: center;
    }
    
    .header-nav__item {
        display: flex;
        align-items: center;
        column-gap: 10px;
    
    }

    .header-nav__item li * {
        text-decoration: none;
        color: white;
        font-weight: bold;
    }

    .header-nav__item li *:hover {
        color: #DDA77B;
        font-weight: bold;
    }

    .search-container {
        position: relative;
    }

    .search-container__input {
        padding-left: 30px;
    }

    .search-container__icon {
        position: absolute;
        top: 10%;
        left: 5px;
        color: black;
    }

    .header-part-func {
        display: flex;
        align-items: center;
        column-gap: 20px;
        margin-left: auto;
        padding-right: 50px;
    }

    .header-part-func__user {
        font-size: 25px;
    }

    .profile-image {
        border-radius: 50%;
    }

    .profile-image:hover {
        cursor: pointer;
    }

    @keyframes slide-out {
        from {
            transform: translateX(300px);
        }
        to {
            transform: translateX(0);
        }
    }
    @keyframes slide-in {
        from {
            transform: translateX(0);
        }
        to {
            transform: translateX(300px);
        }  
    }
    .options-menu {
        --clr-accent: #647AA3;
        display: flex;
        position: absolute;
        z-index: 1000;
        right: 0;
        top: 70px;
        color: black;
        background-color: #5ABCB9;
        border-left: 5px solid var(--clr-accent);
        border-top: 5px solid var(--clr-accent);
        border-bottom: 5px solid var(--clr-accent);
        width: 12%;
    }
    .slide-in {
        animation: slide-in 1s ease both;
    }
    .slide-out {
        animation: slide-out 1s ease both;
    }

    .options-menu-list {
        width: 70%;
        list-style: none;
        display: flex;
        flex-direction: column;
        justify-content: center;
        row-gap: 30px;
        padding: 20px;
        margin: 0px;
    }

    .options-menu-list__item {
        font-size: 20px;
        font-weight: bold;
        color: white;
    }

    .options-menu-list__item:hover {
        color: #DDA77B;
        border-bottom: 3px solid;
        border-image: linear-gradient(to right bottom, #0fdee7, #00bffc, #009aff, #006dff, #3712eb) 1;
        cursor: pointer;
       
    }

    .close-options-menu {
        padding: 20px;
        font-size: 20px;
        margin-left: auto;
        color: white;
        font-weight: bold;
    }

    .close-options-menu:hover {
        color: #DDA77B;
        cursor: pointer;
    }
</style>