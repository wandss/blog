<template>
  <div>
    <CreateEditPost />
    <b-button variant="outline-primary" @click="savePost" >Save</b-button>
  </div>
</template>
<script>
import CreateEditPost from '@/components/CreateEditPost' 

export default {
  name: "PostCreateEditView",
  components: {
    CreateEditPost,
  },
  mounted() {
    this.$store.dispatch('fetchPostStructure')
    if (this.$store.state.token === null) {
      this.$router.push('/') }
  },
  data() {
    return {
      post: {
        title: '',
        text: '',
        tag: '',
        publishDate: '',
      },
    }
  },
  methods: {
    savePost() {
      const blogPost = this.$store.state.newPost.split('\n')
      const stored_title = blogPost.shift()
      let title = stored_title.split('#')
      title = title[title.length -1 ].trim()
      const text = stored_title+"\n"+blogPost.join('\n')
      const blogPostData = {
        title: title,
        text: text,
        tag: '',
        publishDate: '',
        author: this.$store.getters.getUserid
      }
      this.$store.dispatch('createBlogPost', blogPostData)
      this.$store.commit('setNewPost', '')
      // create object and dispatch data to API
    }
  }
}
</script>
