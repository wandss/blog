<template>
  <b-navbar toggleable="lg" type="light" variant="info">
      <b-navbar-brand href="#" id="navbarText">Wand's Blog</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
  
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav id="navbarText">
          <b-nav-item href="#" @click="$router.push('/')">
            Home
          </b-nav-item>
          <b-nav-item href="#" @click="$router.push('/login')">Login</b-nav-item>
          <b-nav-item href="#">Old Posts</b-nav-item>
          <b-nav-item href="#" disabled>About</b-nav-item>
          <b-nav-item href="#" :disabled="this.$store.state.token === null"
            @click="$router.push('/post')">
            New Post
          </b-nav-item>
        </b-navbar-nav>
  
        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
</template>
<script>
export default {
  name: 'NavBar',
}
</script>
<style scoped>
#navbarText {
 margin-left: 1em;
}

</style>
