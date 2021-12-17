<template>
  <div>
    <b-form @submit="onSubmit">
      <b-form-group
        id="input-group-1"
        label="Login:"
        label-for="input-1">
        <b-form-input
          id="input-1"
          type="text"
          placeholder="Enter username"
          v-model="form.username"
          required>
         </b-form-input>
      </b-form-group>
      <b-form-group
        id="input-group-2"
        label="Password:"
        label-for="input-2" >
        <b-form-input
          id="input-2"
          type="password"
          placeholder="Enter password"
          required
          v-model="form.password"
        ></b-form-input>
      </b-form-group>

      <b-button type="submit" variant="primary" class="mt-2">
        Submit
      </b-button>
    </b-form>
  </div>
</template>
<script>
export default {
  name: 'LoginView',
  data() {
    return {
      form: {
        username: 'djangoadmin',
        password: 'djangoadmin'
      },
    }
  },
  methods: {
    onSubmit(event){
      this.$store.dispatch("login", this.form)
      Object.assign(this.form, {username: '', password: ''})
      this.$router.push('/')
    },
  }
}
</script>
