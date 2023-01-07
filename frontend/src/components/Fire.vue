<template>
    <Fireworks
      ref="fw"
      v-if="mounted"
      :autostart="true"
      :options="options"
      :style="{
        top: 0,
        left: 0,
        width: '100%',
        height: '100%',
        position: 'fixed',
        background: '#000'
      }"
    />
  </template>
  
  <script lang="ts" setup>
  import { Fireworks } from '@fireworks-js/vue'
  import type { FireworksOptions } from '@fireworks-js/vue'
  import { ref, watch } from 'vue'
  const mounted = ref(false)

  const props = defineProps({
    iStatus: Boolean
  });

  const fw = ref<InstanceType<typeof Fireworks>>()
  const options = ref<FireworksOptions>({ opacity: 0.5 })

  async function startFireworks() {
    if (!fw.value) return
    fw.value.start()
    await new Promise((resolve) => {
      setTimeout(resolve, 4000);
    })
    await fw.value.waitStop()
    mounted.value =false
  }

  watch(props, () => {
    mounted.value =true
  })

  watch(fw, () => {
    startFireworks();
  })

  </script>
  
  <style scoped>
  body {
    background-color: #000;
  }
  
  .buttons {
    z-index: 1;
    position: absolute;
    display: flex;
    gap: 4px;
  }
  </style>