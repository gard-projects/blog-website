<script>
    export default {
        name: 'TheHeader',
        data() {
            return {
                title: 'Thought Vault',
                description: 'A place to store your thoughts'
            }
        },

        methods: {
            loginUser() {
               return this.$router.push('/login');
            }
        }
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
            <font-awesome-icon icon="circle-user" 
            class="header-part-func__user" 
            @click="loginUser"></font-awesome-icon>
        </div>
    </header>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Raleway&display=swap');
    header {
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

</style>