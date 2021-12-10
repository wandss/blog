import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import { marked } from 'marked'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    posts: [],
    newPost: '',
    newPostFields: {},
    token: null,
    refreshToken: null,
    editPost: {},
  },
  mutations: {
    setPosts(state, payload) {
      state.posts = payload
    },
    setNewPostFormFields(state, payload) {
      state.newPostFields = payload
    },
    setNewPost(state, payload) {
      state.newPost = payload
    },
    setToken(state, payload) {
      state.token = payload
    },
    setRefreshToken(state, payload) {
      state.refreshToken = payload
    },
    setEditPost(state, payload) {
      state.editPost = payload
    },
  },
  getters: {
    getUserid(state) {
      return JSON.parse(atob(state.token.split('.')[1])).user_id
    },
    mdToHtml(state) {
      return marked.parse(state.newPost)
    }
   //filter newPostFields to create a form
   /*postForm(state) {
       let keys = Object.keys(state.newPostFields)
       let fields = []
       keys.forEach(item=>{
           Object.keys(state.newPostFields[item]).forEach(field=>{
               console.log(item, '->',field)
               console.log(state.newPostFields[item][field])
            
           })
       })
       return keys
   }
   */
  },
  actions: {
    fetchPosts(context) {
       //TODO: pass the ordering Query string, dynamically through parameters
       axios.get('http://billie:8000/api/v1/blog/posts/?ordering=-create_date')
        .then(resp => {
            console.log('fetching new posts')
            context.commit('setPosts', resp.data)
        })
       .catch(error=>console.log(error))
    },
    fetchPublishedPosts(context) {
       //TODO: pass the ordering Query string, dynamically through parameters
       axios.get('http://billie:8000/api/v1/blog/posts/published/?ordering=-create_date')
        .then(resp => {
            console.log('fetching new posts')
            context.commit('setPosts', resp.data)
        })
       .catch(error=>console.log(error))
    },
    fetchPostStructure(context) {
       axios.options('http://billie:8000/api/v1/blog/posts/')
        .then(resp=> {
            context.commit('setNewPostFormFields', resp.data.actions.POST)
        })
    },
    login(context, payload) {
        axios.post('http://billie:8000/api/token/', payload)
        .then(resp=>{
            context.commit('setToken', resp.data.access)
            context.commit('setRefreshToken', resp.data.refresh)
            axios.defaults.headers.common['Authorization'] = 'Bearer '+resp.data.access
        })
        .catch(error=>console.log(error))
        context.dispatch("fetchPosts")
    },
    createBlogPost(context, payload) {
        axios.post("http://billie:8000/api/v1/blog/posts/", payload)
        .then(resp => {
            context.dispatch('fetchPosts')
        })
        .catch(error => {
            console.log(error.response)
        })
    },
    updateBlogPost(context, payload) {
      const postID = payload.post_id  

        axios.put("http://billie:8000/api/v1/blog/posts/"+postID, payload)
        .then(resp=>{
            context.dispatch('fetchPosts')
        })
        .catch(error=>console.log(error.response))
    }
  },
  modules: {
  }
})
