<template>
 <b-row align-h="start">
   <b-col>
     <div v-for="post in $store.state.posts">
       <BlogPost :content="mdToHtml(post.text)" :html="true" />
     </div>
   </b-col>
 </b-row>
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
