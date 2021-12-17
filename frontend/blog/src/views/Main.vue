<template>
<div>
  <b-row align-h="start" v-if="$store.state.token !== null">
    <b-col>
      <b-button-group>
        <b-button size="sm" @click="$store.dispatch('fetchPosts')" >
          Show All Posts
        </b-button>
        <b-button size="sm" @click="$store.dispatch('fetchPublishedPosts')">
          Show Published only
        </b-button>
      </b-button-group>
    </b-col>
  </b-row>
  <b-row align-h="start">
    <b-col>
      <div v-for="post in $store.state.posts">
        <BlogPost :content="mdToHtml(post.text)" :html="true" :blogPost="post"/>
      </div>
    </b-col>
  </b-row>
 </div>
</template>

<script>
import { marked } from 'marked'
import BlogPost from '@/components/BlogPost'
export default {
  name: 'Main',
  components: {
    BlogPost,
  },
  props: {
    msg: String
  },
  methods: {
    mdToHtml(text) {
      return marked.parse(text)
    }
  }
}
</script>
