<template>
 <b-row align-h="start">
   <b-col> 
     <BlogPost />
   </b-col>
 </b-row>
</template>

<script>
import BlogPost from '@/components/BlogPost'
export default {
  name: 'Main',
  components: {
    BlogPost,
  },
  props: {
    msg: String
  }
}
</script>
