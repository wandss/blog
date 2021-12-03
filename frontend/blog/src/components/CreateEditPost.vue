<template>
  <b-row>
    <b-col>
      <b-form-textarea
        id="textarea"
        v-model="blogPost"
        placeholder="Use Markdown"
        rows="3"
        max-rows="6"
      >
      </b-form-textarea>
    </b-col>
    <b-col>
      <div  v-html="textPreview"></div>
    </b-col>
  </b-row>
</template>
<script>
import { marked } from 'marked';

export default {
  name: 'CreateEditPost',
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
