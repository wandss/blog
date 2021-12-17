<template>
  <b-navbar toggleable="lg" type="light" variant="info">
      <b-navbar-brand href="#" id="navbarText">Wand's Blog</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
  
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav id="navbarText">
          <b-nav-item href="#" @click="$router.push('/')">
            Home
          </b-nav-item>
          <b-nav-item href="#" v-if="$store.state.token === null"
           @click="$router.push('/login')">
            Login
          </b-nav-item>
          <b-nav-item href="#" v-if="$store.state.token !== null"
            @click="logout" >
            Logout
          </b-nav-item>
          <b-nav-item href="#">Old Posts</b-nav-item>
          <b-nav-item href="#" disabled>About</b-nav-item>
          <b-nav-item href="#" :disabled="this.$store.state.token === null"
            @click="newPost">
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
  //TODO: create method for loggin out
  methods: {
    logout() {
      this.$store.commit('setToken', null)
      this.$store.commit('setPublishedPosts', null)
    },
    newPost() {
      this.$store.commit('setEditPost', {})
      this.$store.commit('setNewPost', '')
      this.$router.push('/post')
    }
  },
}
</script>
<style scoped>
#navbarText {
 margin-left: 1em;
}

</style>
