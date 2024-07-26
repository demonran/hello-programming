<template>
  <header>
    <nav class="wrapper">
      <RouterLink to="/">Home</RouterLink>
      <RouterLink to="/about">About</RouterLink>
      <RouterLink to="/light">Light</RouterLink>
      <RouterLink :isActive="false" to="/" class="dropdown"
        >CSS
        <ul class="dropdown-content">
          <li v-for="item in CssViews" :key="item.path">
            <RouterLink :to="'/css/' + item.path">{{ item.name }} </RouterLink>
          </li>
        </ul>
      </RouterLink>

      <RouterLink :isActive="false" to="/" class="dropdown"
        >Tailwind
        <ul class="dropdown-content">
          <li v-for="item in TailwindViews" :key="item.path">
            <RouterLink :to="'/tailwind/' + item.path">{{ item.name }} </RouterLink>
          </li>
        </ul>
      </RouterLink>
    </nav>
    <ul>
      <li></li>
    </ul>
  </header>
</template>
  
  <script setup lang="ts">
import { RouterLink } from 'vue-router'
import { CssViews, TailwindViews } from '@/constants/index'
</script>
  
  
  
  <style scoped lang="scss">
header {
  background-color: #333;
  display: flex;
  place-items: center;
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
}

nav a.router-link-exact-active {
  background: black;
  color: white;
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 14px 16px;
}

.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  min-width: 200px;
  box-shadow: 0px 8px 16px 0px;
  background: #333;
  z-index: 1;
  list-style-type: none;
  padding: 0;

  a {
    width: 100%;
  }
}

.dropdown:hover .dropdown-content {
  display: block;
}
</style>
  