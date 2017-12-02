<template>
  <div class="Header">
    <router-link to="/">
      <span class="Header__logo">
        <img src="/static/logo.png">
      </span>
    </router-link>
  </div>
</template>

<script>
  export default {

  }
</script>

<style lang="scss">
  @import "../assets/styles/_variables.scss";

  .Header {
    padding: rem(30) rem(40);
    display: flex;
    justify-content: center;

    @include has(logo) {
      font-size: rem(16);
      font-weight: 600;
    }
  }
</style>
