<template>
<div id="card">
  {{blogPost}}
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
  <div>
    <b-button pill variant="success" size="sm" 
      v-if="blogPost.publish_date !== null"
      @click="handlePublish">
      Published
     </b-button>
    <b-button pill variant="outline-success" size="sm" v-else
      @click="handlePublish">
      Publish
    </b-button>
  </div>
</div>
</template>
<script>

export default {
  name: 'BlogPost',
  data(){
    return {
      sample: "Add here all the main texts and blog posts this will be redered by iterating over blog posts. It is the main view.",
    };
  },
  props: {
    blogPost: {
      default: () => {},
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
        //this.$set(blogPost, 'publish_date', new Date().toJSON())
      }
      // TOO creates backed for handling updates
      console.log(blogPost.publish_date)
      this.$store.dispatch('updateBlogPost', blogPost)



    }
  }
}
</script>
<style scoped>
#card {
  padding-top: 0.5em;
  padding-bottom: 0.5em;
}
</style>
