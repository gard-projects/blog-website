<script>
    export default {
        name: 'LoginComponent'
    }
</script>

<template>
   <div class="login-container">
        <h1>Login</h1>
        <div class="login-container__item">
            <p>Username</p>
            <input type="text" placeholder="Enter Username" class="login-container__input">
        </div>
        <div class="login-container__item">
            <p>Password</p>
            <input type="password" placeholder="Enter Password" class="login-container__input"> 
        </div>
        <div class="login-container__item check-user">
            <div class="check-user__body">
                <input type="checkbox" class="check-user__item">
                <p class="check-user__item">Remember me</p>
            </div>
            <p class="check-user__item">Forgot password?</p>
        </div>
        <p class="login-container__item"><router-link to="/signup" class="redirect-user">Don't have an account?</router-link></p>
        <button class="login-button">Login</button>
   </div>
</template>

<style scoped>

    .login-container {
        width: 70%;
        border: 3px solid #98DFAF;
        padding: 10% 20% 10% 20%;
    }
    .login-container h1 {
        border-bottom: 5px solid #8CDEDC;
    }

    .login-container__input {
        width: 80%;
        height: 30px;
    }

    .login-container__item p {
        margin: 20px 0px 5px 0px;
    }

    .check-user {
        display: flex;
        align-items: center;
        column-gap: 200px;
    }

    .check-user__item {
        margin: 20px 0px 0px 0px !important;
        font-size: 13px;
    }

    .check-user__body {
        display: flex;
        column-gap: 5px;
        align-items: center;
    }
    
    .login-button {
        width: 70%;
        height: 30px;
        background-color: #8CDEDC;
        border-radius: 5px;
        margin-top: 20px;
        color: white;
        font-weight: bold;
    }

    .redirect-user {
        text-decoration: none;
        color: black;
        font-size: 13px;
        color: tomato;
    }
</style>