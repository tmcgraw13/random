<template>
  <div class="fix-position">
    <div class="navbar">
      <nav class="flex">
        <router-link to="/">Home</router-link>
        <router-link to="/news">News</router-link>
        <router-link to="/contact">Contact</router-link>
        <router-link to="/games">Games</router-link>
      </nav>
      <nav class="flex">
        <router-link class="active" to="/about">About</router-link>
      </nav>

    </div>
  </div>
  
  <router-view/>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.fix-position{
  position: fixed;
  width: 100%;
  top: 0;
  z-index: 1;
}

  .navbar{
    display: flex;
    justify-content: space-between;
    background-color: #333;
  }

  nav.flex{
    display: flex;
  }

  .active{
    background-color: #04AA6D;
  }

  nav a {
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    text-align: center;
    padding: 14px 16px;
    text-decoration: none;
  }

  a:hover:not(.active) {
    background-color: #111;
  }

</style>
