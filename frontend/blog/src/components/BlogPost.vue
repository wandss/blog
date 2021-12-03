<template>
<div id="card">
  <div v-html="test"></div>
  <b-card title="Title" sub-title="Sub title" bg-variant="light">
    <b-card-text >
      Add here all the main texts and blog posts this will be redered
      by iterating over blog posts. It is the main view.
      Create component for every single blog post.
      Add here all the main texts and blog posts this will be redered
      by iterating over blog posts. It is the main view.
      Create component for every single blog post.
      Add here all the main texts and blog posts this will be redered
      by iterating over blog posts. It is the main view.
      Create component for every single blog post.
      Add here all the main texts and blog posts this will be redered
      by iterating over blog posts. It is the main view.
      Create component for every single blog post.
      Add here all the main texts and blog posts this will be redered
      by iterating over blog posts. It is the main view.
      Create component for every single blog post.
      Add here all the main texts and blog posts this will be redered
      by iterating over blog posts. It is the main view.
      Create component for every single blog post.
      Add here all the main texts and blog posts this will be redered
      by iterating over blog posts. It is the main view.
      Create component for every single blog post.
      Add here all the main texts and blog posts this will be redered
      by iterating over blog posts. It is the main view.
      Create component for every single blog post.
      Add here all the main texts and blog posts this will be redered
      by iterating over blog posts. It is the main view.
      Create component for every single blog post.
      Add here all the main texts and blog posts this will be redered
      by iterating over blog posts. It is the main view.
      Create component for every single blog post.
      Add here all the main texts and blog posts this will be redered
      by iterating over blog posts. It is the main view.
      Create component for every single blog post.
      Add here all the main texts and blog posts this will be redered
      by iterating over blog posts. It is the main view.
      Create component for every single blog post.
      Add here all the main texts and blog posts this will be redered
      by iterating over blog posts. It is the main view.
      Create component for every single blog post.
      Add here all the main texts and blog posts this will be redered
      by iterating over blog posts. It is the main view.
      Create component for every single blog post.
      Add here all the main texts and blog posts this will be redered
      by iterating over blog posts. It is the main view.
      Create component for every single blog post.
      Add here all the main texts and blog posts this will be redered
      by iterating over blog posts. It is the main view.
      Create component for every single blog post.
      Add here all the main texts and blog posts this will be redered
      by iterating over blog posts. It is the main view.
      Create component for every single blog post.
      Add here all the main texts and blog posts this will be redered
      by iterating over blog posts. It is the main view.
      Create component for every single blog post.
      Add here all the main texts and blog posts this will be redered
      by iterating over blog posts. It is the main view.
      Create component for every single blog post.
      Add here all the main texts and blog posts this will be redered
      by iterating over blog posts. It is the main view.
      Create component for every single blog post.
      Add here all the main texts and blog posts this will be redered
      by iterating over blog posts. It is the main view.
      Create component for every single blog post.
    </b-card-text>
    <a href="#" class="card-link">Card link</a>
    <b-link href="#" class="card-link">Another link</b-link>
    <b-link href="#" class="card-link">Tags here</b-link>
  </b-card>
</div>
</template>
<script>
import { marked } from 'marked'

export default {
  name: 'BlogPost',
  data(){
    return {
      markdowntest: "# Some text",
    };
  },
  computed: {
    test() {
      //return marked(this.markdowntest)
      return marked.parse("## computed is fine");
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
