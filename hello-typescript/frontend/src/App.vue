<template>
  <div>
    <header>
      <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />

      <div class="wrapper">
        <nav>
          <RouterLink to="/">Home</RouterLink>
          <RouterLink to="/about">About</RouterLink>
          <RouterLink to="/light">Light</RouterLink>
          <a class="dropdown">CSS
            <ul class="dropdown-content">
            <li> <RouterLink to="/css/translucent-borders">半透明边框 </RouterLink></li>
            <li> <RouterLink to="/css/multiple-borders">多层边框 </RouterLink></li>
            <li> <RouterLink to="/css/translucent-borders">半透明边框 </RouterLink></li>
            <li> <RouterLink to="/css/translucent-borders">半透明边框 </RouterLink></li>
          </ul>
          </a>
          
         
        </nav>
      </div>
    </header>

    <RouterView />
  </div>
</template>

<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>



<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
  display: flex;
  place-items: center;
  padding-right: calc(var (--section-gap) / 2);
}

.logo {
  display: block;
  width: 50px;
  margin: 0 2rem 0 0;
}



nav {
  width: 100%;
  font-size: 1rem;
  text-align: left;
  /* margin-left: -1rem; */
  padding: 1rem 0;
  margin-top: 1rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}



header .wrapper {
  display: flex;
  place-items: flex-start;
  flex-wrap: wrap;
}

.dropdown-content {
  display: none;
  position:absolute;
  box-shadow: 0px 8px 16px 0px;
  z-index: 1;
  list-style-type: none;
  padding: 0;
}

.dropdown:hover .dropdown-content {
  display: block;
}


</style>
