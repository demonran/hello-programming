<template>
  <main>
    <div class="progress-outer">
      <div class="progress-enter">
        <div class="progress-bg">
          <div class="progress-value">60%</div>
        </div>
      </div>
    </div>
  </main>
</template>

<style lang="scss" scoped>
main {
  display: flex;
  justify-content: center;
  padding: 80px 0px;
}

.progress-outer {
  width: 60%;
  height: 20px;
  border-radius: 8px;
  border: black solid 1px;
  padding: 2px;
  position: relative;

  .progress-enter {
    height: 14px;
    background: rgba(180, 160, 120, 0.2);
    border-radius: 6px;

    .progress-bg {
      width: 60%;
      height: inherit;
      border-radius: 6px;
      background: repeating-linear-gradient(
        -45deg,
        #d9cfbb 25%,
        #c3b393 0,
        #c3b393 50%,
        #d9cfbb 0,
        #d9cfbb 75%,
        #c3b393 0
      );
      background-size: 30px 30px;
      animation: panoramic 20s linear infinite;

      .progress-value {
        top: -50px;
        position: absolute;
        left: calc(60% - 50px);
        z-index: 1;

        border-radius: 30px;
        width: 100px;
        padding: 5px 10px;
        text-align: center;
        background: rgb(146, 146, 64);
      }

      .progress-value::after {
        content: ' ';
        position: absolute;
        top: 100%;
        left: 50%;
        border-style: solid;
        border-width: 5px;
        border-color: rgb(146, 146, 64) transparent transparent transparent;
      }
    }
  }
}

@keyframes panoramic {
  to {
    background-position: 200% 0;
  }
}
</style>
