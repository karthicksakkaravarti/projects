import axiosIns from '@/plugins/axios.js'
import { status_color, exception_rest_api_handler, extract_api_data } from '@/helper'

const addons_path = '/addons/apps/project'
const state = {
  projects: [],
  project: {},
}

const getters = {
  allProjects: (state) => state.projects,
  singleProject: (state) => state.project,
}

const mutations = {
  SET_PROJECTS(state, projects) {
    state.projects = projects
  },
  SET_PROJECT(state, project) {
    state.project = project
  },
  ADD_PROJECT(state, project) {
    state.projects.push(project)
  },
}

const actions = {
  GET_PROJECTS({ commit }, query = '') {
    return new Promise((resolve, reject) => {
      axiosIns.get(`${addons_path}/api/projects/${query}`)
        .then(response => {
          commit('SET_PROJECTS', response.data)
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  GET_PROJECT({ commit }, id) {
    return new Promise((resolve, reject) => {
      axiosIns.get(`${addons_path}/api/projects/${id}/`)
        .then(response => {
          commit('SET_PROJECT', response.data)
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  CREATE_PROJECT({ commit }, payload) {
    let data = {}
    if (payload && payload.not_execute_extract) {
      data = payload.data
    } else {
      data = extract_api_data(payload.data ? payload.data : [])
    }
    return new Promise((resolve, reject) => {
      axiosIns.post(`${addons_path}/api/projects/`, data)
        .then(response => {
          resolve(response)
        })
        .catch(error => {
          reject(error)
        })
    })
  },
  // ... existing TodoStore actions ...
}

export const ProjectStore = {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}
