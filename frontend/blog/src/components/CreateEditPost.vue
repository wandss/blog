<template>
  <b-row>
    <b-col cols="5">
      <b-form-textarea
        id="textarea"
        v-model="text"
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
import BlogPost from '@/components/BlogPost'

export default {
  name: 'CreateEditPost',
  components: { BlogPost }, 
  computed: {
    text: {
      get() {
        return this.$store.state.newPost
      },
      set (value) {
        this.$store.commit('setNewPost', value);
      }
    },
    textPreview() {
      return this.$store.getters.mdToHtml
    },
  },
}
</script>
