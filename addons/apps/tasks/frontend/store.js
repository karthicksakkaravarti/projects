import axiosIns from '@/plugins/axios.js'
import { extract_api_data } from '@/helper'

const addons_path = '/addons/apps/tasks'
const state = {
    tasks: [],
    task: {}
}

const getters = {
    allTasks: state => state.tasks,
    getTask: state => state.task
}

const mutations = {
    SET_TASKS(state, tasks) {
        state.tasks = tasks
    },
    SET_TASK(state, task) {
        state.task = task
    }
}

const actions = {
    GET_TASKS({ commit }, query='') {
        return new Promise((resolve, reject) => {
            axiosIns.get(`${addons_path}/api/tasks/${query}`)
                .then(response => {
                    commit('SET_TASKS', response.data.results)
                    resolve(response)
                })
                .catch(error => {
                    reject(error)
                })
        })
    },
    CREATE_TASK({ commit }, payload) {
        let data = extract_api_data(payload.data || {})
        return new Promise((resolve, reject) => {
            axiosIns.post(`${addons_path}/api/tasks/`, data)
                .then(response => {
                    resolve(response)
                })
                .catch(error => {
                    reject(error)
                })
        })
    },
    PATCH_TASK({ commit }, payload) {
        return new Promise((resolve, reject) => {
            axiosIns.patch(`${addons_path}/api/tasks/${payload.id}/`, payload.data)
                .then(response => {
                    resolve(response)
                })
                .catch(error => {
                    reject(error)
                })
        })
    },
    DELETE_TASK({ commit }, id) {
        return new Promise((resolve, reject) => {
            axiosIns.delete(`${addons_path}/api/tasks/${id}/`)
                .then(response => {
                    resolve(response)
                })
                .catch(error => {
                    reject(error)
                })
        })
    },
}

export const TasksStore = {
    namespaced: true,
    state,
    getters,
    mutations,
    actions
}