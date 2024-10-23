import axiosIns from '@/plugins/axios.js'
import { status_color, exception_rest_api_handler, extract_api_data } from '@/helper'

const addons_path = '/addons/apps/repositories'
const state = {}

const getters = {}

const mutations = {}

const actions = {
    GET_repositories({ commit }, query=''){
        return new Promise((resolve, reject) => {
            axiosIns.get(addons_path+ '/api/repositories/' + query)
            .then(data => {
              resolve(data)
            })
            .catch(err => {
              reject(err)
            })
        })
    },
    CREATE_repositories({ commit }, payload) {
        let data = {}
        if (payload && payload.not_execute_extract) {
          data = payload.data
        } else {
          data = extract_api_data(payload.data ? payload.data : [])
        }
        return new Promise((resolve, reject) => {
          axiosIns.post(`${addons_path}/api/repositories/`, data)
            .then(response => {
              resolve(response)
            })
            .catch(error => {
              reject(error)
            })
        })
    },
    FETCH_repository_files({ commit }, repositoryId) {
        return new Promise((resolve, reject) => {
            axiosIns.get(`/addons/apps/repositories/api/repositories/${repositoryId}/files/`)
                .then(response => {
                    commit('SET_repositoryFiles', { repositoryId, files: response.data.files })
                    resolve(response)
                })
                .catch(err => {
                    reject(err)
                })
        })
    },

    CREATE_file({ commit }, { repositoryId, filePath, content }) {
        return new Promise((resolve, reject) => {
            axiosIns.post(`/addons/apps/repositories/api/repositories/${repositoryId}/create_file/`, {
                file_path: filePath,
                content: content
            })
            .then(response => {
                resolve(response)
            })
            .catch(err => {
                reject(err)
            })
        })
    },
}

export const RepositoriesStore = {
    namespaced: true,
    state: {
        repositoryFiles: {}
    },
    getters: {
        getRepositoryFiles: (state) => (repositoryId) => {
            return state.repositoryFiles[repositoryId] || []
        },
    },
    mutations: {
        SET_repositoryFiles(state, { repositoryId, files }) {
            if (!state.repositoryFiles) {
                state.repositoryFiles = {}
            }
            state.repositoryFiles[repositoryId] = files
        },
    },
    actions
}
  
