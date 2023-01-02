<template>
    <div>
      <button class="cell" :disabled="value.status !== ''">{{ value.move }}</button>
    </div>
</template>

<script>
  export default {
    props: {
      value: {String,String}
    }
  }
</script>
<style>
  .cell {
    width: 64px;
    height: 64px;
    border: 2px solid rgb(75,75,75);
    font-size: 42px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
</style>