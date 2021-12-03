<template>
  <div>
    <Navbar />
    <b-container fluid class="bv-example-row">
      <b-row align-h="start">
      <b-col> 
        <BlogPost />
        <BlogPost />
      </b-col>
    </b-row>
    </b-container>
  </div>
</template>
<script>
import Navbar from '@/components/Navbar'
import BlogPost from '@/components/BlogPost'

export default {
  name: 'App',
  components: {
    Navbar,
    BlogPost,
  },
}
</script>

<style>
</style>
