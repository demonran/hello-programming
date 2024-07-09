<template>
  <div>
    <LayoutHeader></LayoutHeader>

    <RouterView />
  </div>
</template>
  
  <script setup lang="ts" name="layout">
import { defineAsyncComponent } from 'vue'

const LayoutHeader = defineAsyncComponent(() => import('./header.vue'))
</script>
  
  
  
<style scoped>

</style>
  