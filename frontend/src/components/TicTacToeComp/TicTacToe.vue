<template>
  <p>{{ board }}</p>
  <div class="center">
    <div class="tictactoe-board">
      <div v-for="(n, c) in 3">
        <div v-for="(n, r) in 3">
          <cell @click="performMove(c, r)" :value="board[c][r]"></cell>
        </div>
      </div>
    </div>
  </div>
  </template>
<script>
import Cell from './Cell.vue'
import axios from "axios";
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';

  export default {
    components: { Cell },
    data() { return {
      board: [
          ['', '', ''],
          ['', '', ''],
          ['', '', '']
        ],
      spot: [1,1]
    } },

    methods: {
      performMove(column, row) {
        if (this.board[column][row] !== '') {
          // Invalid move.
          return;
        }
        this.board[column][row] = 'X';
        console.log('this is my column', column)
        console.log('this is my row', row)
        this.spot = [row,column]
        this.postBoard()
      },
      postBoard() {
      const path = 'https://random-backend-dev2.us-east-1.elasticbeanstalk.com/test';
      axios
        .post(path,{
          board: this.board,
        }, { useCredentails: false })
        .then((res) => {
          console.log(res.data)
          this.board = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    }
  }
</script>
<style>
  .tictactoe-board {
    display: flex;
    flex-wrap: wrap;
    width: 204px;
    height: 204px;
  }
  .center{
    overflow: hidden;
    position: absolute;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center; /*centers items on the line (the x-axis by default)*/
    align-items: center; /*centers items on the cross-axis (y by default)*/
  }
</style>