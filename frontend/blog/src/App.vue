<template>
  <div>
    <Navbar />
    <div id="mainApp">
      <b-container fluid class="bv-example-row">
        <router-view></router-view>
      </b-container>
    </div>
  </div>
</template>
<script>
import Navbar from '@/components/Navbar'
import PostCreateEditView from '@/views/PostCreateEditView'

export default {
  name: 'App',
  components: {
    Navbar,
  },
  mounted() {
    this.$store.dispatch('fetchPublishedPosts')
  }
}
</script>

<style>
#mainApp {
  margin-top: 1em;
}
</style>
