<template>
  <button @click="getMessage">Click Me</button>
  <div>
    <h1>Page 5</h1>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from "axios";
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';

export default {
  name: "About",
  data() {
    return {
      msg: "",
    };
  },
  methods: {
    getMessage() {
      const path = "http://127.0.0.1:8082/ping";
      axios
        .get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
