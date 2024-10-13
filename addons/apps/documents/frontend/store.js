import axiosIns from '@/plugins/axios.js'
import { status_color, exception_rest_api_handler, extract_api_data } from '@/helper'

const addons_path = '/addons/apps/documents'
const state = {}

const getters = {}

const mutations = {}

const actions = {
    GET_DOCUMENTS({ commit }, query=''){
        return new Promise((resolve, reject) => {
            axiosIns.get(addons_path+ '/api/documents/' + query)
            .then(data => {
              resolve(data)
            })
            .catch(err => {
              reject(err)
            })
        })
    },
    CREATE_DOCUMENT({ commit }, payload) {
        console.log(payload)
        let data = {}
        if (payload && payload.not_execute_extract) {
          data = payload.data
        } else {
          data = extract_api_data(payload.data ? payload.data : [])
        }
        return new Promise((resolve, reject) => {
          axiosIns.post(`${addons_path}/api/documents/`, data)
            .then(response => {
              resolve(response)
            })
            .catch(error => {
              reject(error)
            })
        })
    },
    // Patch Document
    PATCH_DOCUMENT({ commit }, payload) {
        // let data = {}
        // if (payload && payload.not_execute_extract) {
        //   data = payload.data
        // } else {
        //   data = extract_api_data(payload.data ? payload.data : [])
        // }
        return new Promise((resolve, reject) => {
          axiosIns.patch(`${addons_path}/api/documents/${payload.id}/`, payload.data)
            .then(response => {
              resolve(response)
            })
            .catch(error => {
              reject(error)
            })
        })
    },
    // Delete Document
    DELETE_DOCUMENT({ commit }, id) {
        return new Promise((resolve, reject) => {
            axiosIns.delete(`${addons_path}/api/documents/${id}/`)
              .then(response => {
                resolve(response)
              })
              .catch(error => {
                reject(error)
              })
          })
    }
}

export const DocumentsStore = {
    namespaced: true,
    state,
    getters,
    mutations,
    actions
}
  