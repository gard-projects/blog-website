<template>
  <the-header></the-header>
  <main>
    <router-view></router-view>
  </main>
</template>

<script>
import TheHeader from './components/TheHeader.vue'

export default {
  name: 'App',
  components: { TheHeader },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
  body {
    margin: 0;
    font-family: 'Roboto', sans-serif;
  }

  main {
    width: 50%;
    margin: auto;
    margin-top: 100px;
    display: flex;
    justify-content: center;
  }
</style>
