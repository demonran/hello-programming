<template>
  <div class="container">
    <div class="item" ref="cardRef1">
    </div>
    <div class="item" ref="cardRef2">
    </div>
    <div class="item" ref="cardRef3">
    </div>
  </div>
</template>
<script setup lang="ts" name="LightView">
import { useLightCard } from '@/hooks/use-light-card';

const { cardRef: cardRef1 } = useLightCard();
const {  cardRef: cardRef2 } = useLightCard({
  light: {
    color: '#fff',
  }
});
const { cardRef: cardRef3 } = useLightCard();


</script>
<style lang="scss" scoped>
.container {
  background: black;
  width: 100%;
  height: 100%;
  padding: 200px;
  display: flex;
  justify-content: space-between;

  .item {
    position: relative;
    width: 300px;
    height: 300px;
    background: #1c1c1f;
    margin: 10px;
    border: 1px solid rgba(255, 255, 255, 0.1);

  }
}
</style>
