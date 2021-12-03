<template>
  <div>
    <Navbar />
    <CreateEditPost />
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
import CreateEditPost from '@/components/CreateEditPost'

export default {
  name: 'App',
  components: {
    Navbar,
    BlogPost,
    CreateEditPost,
  },
}
</script>

<style>
</style>
