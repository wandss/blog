import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    posts: []
  },
  mutations: {
    setPosts(state, payload) {
      payload.forEach(item=>state.posts.push(item))
      //Change, since it's an array
    }
  },
  actions: {
    fetchPosts(context) {
       axios.get('http://billie:8000/api/v1/blog/posts/')
        .then(resp => {
            console.log(resp.data)
            context.commit('setPosts', resp.data)
        })
       //.then(resp=>{context.commit('setPosts', resp.data)})
       .catch(error=>console.log(error))
    }
  },
  modules: {
  }
})
