<template>
    <div>
      <p>Games</p>
      <h1>Page 4</h1>
      <TicTacToeVue/>
    </div>
  </template>
  
  <script>
  import TicTacToeVue from '@/components/TicTacToeComp/TicTacToe.vue';
  export default {
    name: 'Games',
    components: {TicTacToeVue}
  };
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
  
  </style>