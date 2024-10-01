import axiosIns from '@/plugins/axios.js'

const addons_path = '/addons/apps/todo'
const state = {}

const getters = {}

const mutations = {}

const actions = {
    GET_TODO({ commit }, query=''){
        return new Promise((resolve, reject) => {
            axiosIns.get(addons_path+ '/api/todos/' + query)
            .then(data => {
              resolve(data)
            })
            .catch(err => {
              reject(err)
            })
        })
      },
      POST_TODO({ commit }, payload){
        return new Promise((resolve, reject) => {
            axiosIns.post(addons_path+ '/api/todos/' , payload)
            .then(data => {
              resolve(data)
            })
            .catch(err => {
              reject(err)
            })
        })
      },
      DELETE_TODO({ commit }, query=''){
        return new Promise((resolve, reject) => {
            axiosIns.delete(addons_path+ '/api/todos/' + query)
            .then(data => {
              resolve(data)
            })
            .catch(err => {
              reject(err)
            })
        })
      },
}

export const TodoStore = {
    namespaced: true,
    state,
    getters,
    mutations,
    actions
}
  