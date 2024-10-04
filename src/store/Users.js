import Axios from '@/plugins/axios.js'

const state = {
    // UsersList: [],
  }
  
  const getters = {
    // UsersList: state => state.UsersList,
  }

  const mutations = {
    // mutation__userslist(state, value) {
    //   state.UsersList = value
    // },
  }

  const actions = {
    // Actions
    // SetUsersList({ commit }, value) {
    //   commit('mutation__userslist', value)
    // },

    // Api's
    API_USERS({ commit }, query = '') {
        return new Promise((resolve, reject) => {
          Axios.get('pm/api/userinfo/' + query)
            .then(data => {
              resolve(data)
              commit('mutation__userslist', data.data.results)
            })
            .catch(err => {
              reject(err)
            })
        })
      },
      API_MASTER_USERS({ commit }, query = '') {
        return new Promise((resolve, reject) => {
          Axios.get('pm/api/users/' + query)
            .then(data => {
              resolve(data)
            })
            .catch(err => {
              reject(err)
            })
        })
      },

  }
  export const UsersStore = {
    namespaced: true,
    state,
    getters,
    mutations,
    actions
  }
  