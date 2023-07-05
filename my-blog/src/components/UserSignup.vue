<script>
import axios from 'axios';

    export default {
        name: 'SignupComponent',
        data() {
            return {
                emailTaken: false,
                usernameTaken: false,
                password: '',
                email: '',
                userName: '',
                confirmedPassword: '',
                mismatchedPassword: false,
                passwordType: 'password'
            }
        },

        watch: {
            async userName(newUsername) {
                try {
                    console.log(newUsername)
                    const request = await axios.get(`/api/check_username?user_name=${newUsername}`);
                    let response = request.data;
                    console.log(response);
                    if(response) {
                        this.usernameTaken = true;
                    } else {
                        this.usernameTaken = false;
                    }
                } catch(error) {
                    console.log('An error has occured: ', error)
                }
            },
            
            async email(newEmail) {
                try {
                    const request = await axios.get(`/api/check_email?email=${newEmail}`);
                    let response = request.data;
                    if(response) {
                        this.emailTaken = true;
                    } else {
                        this.emailTaken = false;
                    }
                } catch(error) {
                    console.log('An error has occured: ', error)
                }
            },
            password() {
                if(this.password == '') {
                    this.mismatchedPassword = false;
                }
            },

            confirmedPassword(newConfirmPassword) {
                this.mismatchedPassword = this.password !== newConfirmPassword;
            }
            },

        methods: {
            showPassword() {
                this.passwordType = this.passwordType === 'password' ? 'text' : 'password';
            },
            async createUser() {
                try {
                    const request = await axios.post('/api/register_user', {
                        user_name: this.userName,
                        email: this.email,
                        password: this.password
                    });
        
                    let response = request.data;
                    if(response) {
                        this.$router.push('/login');
                    }
                } catch(error) {
                    console.log('An error has occured: ', error)
                }
            }
        }
    }
</script>

<template>
    <div class="signup-container">
        <h1>Signup</h1>
        <div class="signup-container__item">
            <p>Username</p>
            <div>
                <input type="text" placeholder="Enter Username" class="signup-container__input" v-model="userName">
                <p class="not-available" v-if="usernameTaken">Username is in use!</p>
            </div>   
        </div>

        <div class="signup-container__item">
            <p>Email</p>
            <div>
                <input type="email" placeholder="Enter Email" class="signup-container__input" v-model="email">
                <p class="not-available" v-if="emailTaken">Email is in use!</p>
            </div>
        </div>

        <div class="signup-container__item">
            <p>Password</p>
            <div>
                <input :type="passwordType" placeholder="Enter Password" class="signup-container__input" v-model="password">
                <font-awesome-icon icon="eye" class="signup-container__icon" @click="showPassword"></font-awesome-icon>
            </div>
        </div>
        <div class="signup-container__item">
            <p>Confirm Password</p>
            <div>
                <input :type="passwordType" placeholder="Confirm Password" class="signup-container__input" v-model="confirmedPassword">
                <font-awesome-icon icon="eye" class="signup-container__icon" @click="showPassword"></font-awesome-icon>
                <p class="not-available" v-if="mismatchedPassword">Password does not match!</p>
            </div>
            
        </div>

        <p class="signup-container__item"><router-link to="/login" class="redirect-user">Already have an account?</router-link></p>
        <button class="signup-user" @click="createUser">Create user</button>
    </div>
</template>

<style scoped>

    .signup-container {
        border: 3px solid #98DFAF;
        padding: 10% 20% 10% 20%;
        width: 70%;
    }
    .signup-container h1 {
        border-bottom: 5px solid #8CDEDC;
        width: 80%;
    }

    .signup-user {
        margin-top: 20px;
        width: 70%;
        height: 30px;
        background-color: #8CDEDC;
        color: white;
        font-weight: bold;
        border-radius: 5px;
    }

    .signup-container__item div {
        display: flex; 
        align-items: center;
        column-gap: 10px;
    }

    .signup-container__input {
        width: 70%;
        height: 30px;
    }

    .redirect-user {
        text-decoration: none;
        color: black;
        font-size: 13px;
        color: tomato;
    }

    .not-available {
        background: -webkit-linear-gradient( #C45AB3, #631A86);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 13px;
    }
</style>