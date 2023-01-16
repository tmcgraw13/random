<template>
  <Fire :iStatus="isGameStatus"/>
  <div class="game-stats">
    <p>{{ status }}</p>
    <p>{{ board }}</p>
    <p>Reset? {{ iReset }}</p>
     <p> Is there a game status?: {{ isGameStatus }}</p>
  </div>
  
  <div class="center">
    <div class="tictactoe-board">
      <div v-for="(n, c) in 3">
        <div v-for="(n, r) in 3">
          <cell @click="performMove(c, r)" :value="{move:board[c][r],status:status}"></cell>
        </div>
      </div>
    </div>
  </div>
  </template>
<script>
import Cell from './Cell.vue'
import axios from "axios";
import Fire from '../Fire.vue'

axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';

  export default {
    components: { Cell, Fire },
    props: {
      iReset: Boolean
    },
    watch: {
      iReset: function(value) {
          this.resetGame();
        }
    },
    data() { return {
      board: this.initBoard(),
      status: '',
      isGameStatus: false
    } },
    methods: {
      resetGame(){
        this.board = this.initBoard();
        this.status = '';
        this.isGameStatus = false;
      },
      initBoard(){
        return [
          ['', '', ''],
          ['', '', ''],
          ['', '', '']
        ]
      },
      performMove(column, row) {
        if (this.board[column][row] !== '') {
          // Invalid move.
          return;
        }
        this.board[column][row] = 'X';
        this.postBoard()
      },
      postBoard() {
      const path = 'http://127.0.0.1:8082/test';
      axios
        .post(path,{
          board: this.board,
        }, { useCredentails: false })
        .then((res) => {
          this.board = res.data.board;
          this.status = res.data.status;
          this.isGameStatus = this.checkStatus(res.data.status)
        })
        .catch((error) => {
          console.error(error);
        });
      },
      checkStatus(currentStat){
        console.log(currentStat)
        if(currentStat != ''){
          return true
        }
        else {
          return false}
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
  .game-stats {
    display: flex;
    width: 100%;
    color: red;
    position: absolute;
    justify-content: space-between;
  }
</style>