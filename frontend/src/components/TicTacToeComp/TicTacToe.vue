<template>
  <div class="center">
    <div class="tictactoe-board">
      <div v-for="(n, i) in 3">
        <div v-for="(n, j) in 3">
          <cell @click="performMove(i, j)" :value="board[i][j]"></cell>
        </div>
      </div>
    </div>
  </div>
  </template>
<script>
import Cell from './Cell.vue'
  export default {
    components: { Cell },
    data() { return {
      board: [
          ['', '', ''],
          ['', '', ''],
          ['', '', '']
        ]
    } },

    methods: {
      performMove(x, y) {
        if (this.board[x][y] !== '') {
          // Invalid move.
          return;
        }
        this.board[x][y] = 'x';
        // TODO implement some AI super-overlord algorithm that will calculate
        //  the computers move.
      }
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