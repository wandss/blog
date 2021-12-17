<template>
<div id="card">
  <b-card bg-variant="light" v-if="html">
    <b-card-text v-html="content">
      {{ content }}
    </b-card-text>
    </b-card-text>
    <a href="#" class="card-link">Card link</a>
    <b-link href="#" class="card-link">Another link</b-link>
    <b-link href="#" class="card-link">Tags here</b-link>
  </b-card>
  <b-card :title="title" :sub-title="subtitle" bg-variant="light" v-else >
    <b-card-text>
      {{ content }}
    </b-card-text>
    </b-card-text>
    <a href="#" class="card-link">Card link</a>
    <b-link href="#" class="card-link">Another link</b-link>
    <b-link href="#" class="card-link">Tags here</b-link>
  </b-card>
  <div 
    v-if="Object.keys(blogPost).length !== 0 && $store.state.token !== null"
    class="mt-2">
     <b-button pill id="publish"
     :variant="blogPost.publish_date!==null?'success':'outline-success'" 
       size="sm" 
       @click="handlePublish" >
       {{blogPost.publish_date !== null? 'Published':'Publish'}}
      </b-button>
     <b-button pill variant="outline-warning" size="sm" 
      @click="editPost">
       Edit
     </b-button>
  </div>
</div>
</template>
<script>

export default {
  name: 'BlogPost',
  props: {
    blogPost: {
      default: function (value){
        return {}
      }, 
      type: Object
    },
    content: {
      default: "Some default Text",
      type: String
    },
    html: {
      default: false,
      type: Boolean,
    },
    title: {
      type: String,
      default: "Please enter a Title...."
    },
    subtitle: {
      type: String,
      default: "Subtitle"
    },
  },
  methods: {
    handlePublish() {
      let blogPost = {...this.blogPost}
      if (this.blogPost.publish_date !== null) {
        this.$set(blogPost, 'publish_date', null)
      }
      else {
        this.$set(blogPost, 'publish_date', new Date())
      }
      this.$store.dispatch('updateBlogPost', blogPost)
    },
    editPost() {
      this.$store.commit('setEditPost', this.blogPost)
      this.$store.commit('setNewPost', this.blogPost.text)
      if (this.$store.state.token === null) {
        this.$router.push('/login')
      }
      else {
        this.$router.push('/post')
      }
    }
  }
}
</script>
<style scoped>
#card {
  padding-top: 0.5em;
  padding-bottom: 0.5em;
}
#publish {
  margin-right: 0.5em;
}
</style>
