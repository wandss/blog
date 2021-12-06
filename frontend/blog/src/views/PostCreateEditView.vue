<template>
  <div>
    <CreateEditPost />
    <b-button variant="outline-primary">Save</b-button>
  </div>
</template>
<script>
import CreateEditPost from '@/components/CreateEditPost' 

export default {
  name: "PostCreateEditView",
  components: {
    CreateEditPost,
  },
}
</script>
