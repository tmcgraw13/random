<template>
    <div>
      <p>Games</p>
      <h1>Page 4</h1>
      <button @click="reset = !reset">Reset Game</button>
      <TicTacToeVue :iReset="reset"/>
    </div>
  </template>
  
  <script>
  import TicTacToeVue from '@/components/TicTacToeComp/TicTacToe.vue';
  export default {
    name: 'Games',
    components: {TicTacToeVue},
    data(){
      return{
        reset: false
      }
    }
  };
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  
  </style>