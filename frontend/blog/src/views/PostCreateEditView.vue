<template>
  <div>
    <CreateEditPost />
    <b-button pill :variant="publishDate===null?'outline-success':'success'" 
      size="sm"
      @click="publishPost" >
        Publish
     </b-button>
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
  data () {
    return {
      publishDate: null,
    }
  },
  mounted() {
    this.$store.dispatch('fetchPostStructure')
    if (this.$store.state.token === null) {
      this.$router.push('/') 
    }
    if (Object.keys(this.$store.state.editPost).length !== 0) {
      this.publishDate = this.$store.state.editPost.publish_date
    }
  },
  methods: {
    publishPost() {
      if (this.publishDate === null) {
        this.publishDate = new Date()
      }
      else {
        this.publishDate = null
      }
    },
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
        publish_date: this.publishDate, 
        author: this.$store.getters.getUserid
      }
      if (Object.keys(this.$store.state.editPost).length === 0) {
        this.$store.dispatch('createBlogPost', blogPostData)
      }
      else {
        const editPost = Object.assign(this.$store.state.editPost,
                                       blogPostData)
        this.$store.dispatch('updateBlogPost', editPost)
      }
      this.$store.commit('setNewPost', '')
      this.$store.commit('setEditPost', {})
      this.$router.go(-1)
    }
  }
}
</script>
