<template>
  <b-row>
    <b-col cols="5">
      <b-form-textarea
        id="textarea"
        v-model="blogPost"
        placeholder="Use Markdown..."
        rows="3"
        max-rows="6"
      >
      </b-form-textarea>
    </b-col>
    <b-col>
      <BlogPost :content="textPreview" :html="true"/>
    </b-col>
  </b-row>
</template>
<script>
import { marked } from 'marked'
import BlogPost from '@/components/BlogPost'

export default {
  name: 'CreateEditPost',
  components: {BlogPost}, 
  data() {
    return {
      blogPost: '',
    }
  },
  computed: {
    textPreview() {
      return marked.parse(this.blogPost);
    }
  }
}
</script>
