import appConfigStoreModule from '@core/@app-config/appConfigStoreModule'
import Vue from 'vue'
import Vuex from 'vuex'
import axiosIns from '@/plugins/axios.js'
import app from './app'



import { UsersStore } from './Users'
import { TodoStore } from '../../addons/apps/todo/frontend/store.js'
import { ProjectStore } from '../../addons/apps/project/frontend/store.js'
import { RepositoriesStore } from '../../addons/apps/repositories/frontend/store.js'

Vue.use(Vuex)

const storeModules = require.context('../../addons/apps', true, /frontend\/store\.js$/)

let dynamicModules = {}

storeModules.keys().forEach(modulePath => {
  const moduleName = modulePath.split('/')[1] // Extract the module name from the modulePath
  const value = storeModules(modulePath)
  console.log(value)
  if (value[`${moduleName.charAt(0).toUpperCase() + moduleName.slice(1)}Store`]) {
    // If a module-specific store export exists, use it
    dynamicModules[`${moduleName.charAt(0).toUpperCase() + moduleName.slice(1)}Store`] =
      value[`${moduleName.charAt(0).toUpperCase() + moduleName.slice(1)}Store`]
  }
})
console.log(dynamicModules)
export default new Vuex.Store({
  state: {
    appName: 'Everest', // Used in sidebar
    user: {},
    preference: {},
    Drawer: {
      DrawerModel: false,
      DrawerShowAppBar: false,
      DrawerSize: '35%',
      DrawerFormType: '',
      DrawerForm: [],
      DrawerFormSubmit: {},
      DrawerLoader: true,
      DrawerFormAPICall: false,
      DrawerFormTitle: '',
      DrawerExtraParam: '',
      DrawerFilterForm: false,
      DrawerFilterStore: '',
    }, // Used to open drawer

    SecondDrawer: {
      DrawerModel: false,
      DrawerShowAppBar: false,
      DrawerSize: '35%',
      DrawerFormType: '',
      DrawerForm: [],
      DrawerFormSubmit: {},
      DrawerLoader: true,
      DrawerFormAPICall: false,
      DrawerExtraParam: '',
    }, // Used to open customer drawer
    Dialog: {
      FullDialog: false, // Not,
      DialogSize: '400',
      Dialog: false,
      Title: '',
      RefName: '', // remove this and hardcode
      DialogForm: [],
      FormName: '',
      Loader: false,
      SubmitButton: {},
      DialogExtraParam: '',
      DialogEditType: '',
      DialogWindow: 1,
    },
    ConfirmationDialog: {
      Dialog: false,
      Title: '',
      Loader: false,
      Body: '',
      DialogExtraParam: '',
      DialogEditType: '',
      SubmitButton: {},
    },
    Apps: [],
    Snackbar: {
      bar: false,
      text: '',
      color: 'success',
    },
  },
  getters: {
    Drawer: state => state.Drawer,
    Dialog: state => state.Dialog,
    Apps: state => state.Apps,
    Snackbar: state => state.Snackbar,
  },
  mutations: {
    mutation__user(state, value) {
      state.user = Object.assign(state.user, value)
    },
    mutation__preference(state, value) {
      state.preference = Object.assign(state.preference, value)
    },
    mutation__drawer(state, value) {
      state.Drawer = Object.assign(state.Drawer, value)
    },
    mutation__dialog(state, value) {
      state.Dialog = Object.assign(state.Dialog, value)
    },
    mutation__normaldialog(state, value) {
      state.Dialog = Object.assign(state.Dialog, value)
    },
    mutation__confirmationdialog(state, value) {
      state.ConfirmationDialog = Object.assign(state.ConfirmationDialog, value)
    },
    mutation__snackbar(state, value) {
      state.Snackbar = value
    },
    mutation__second_drawer(state, value) {
      state.SecondDrawer = Object.assign(state.SecondDrawer, value)
    },
    mutation__reset_error_message(state) {
      try {
        for (const drawerField of state.Drawer.DrawerForm) {
          drawerField.error_message = null
        }
      } catch (_) {}
    },
    mutation__set_errors(state, value) {
      console.log('mutation__set_errors', value)

      // Drawer
      try {
        for (var [key, value] of Object.entries(value)) {
          // Drawer
          for (const drawerField of state.Drawer.DrawerForm) {
            if (drawerField.dbfield == key) {
              drawerField.error_message = value[0]
            }
          }

          // Dialog
          for (const DialogFormdrawerField of state.Dialog.DialogForm) {
            if (DialogFormdrawerField.dbfield == key) {
              DialogFormdrawerField.error_message = value[0]
            }
          }
        }
      } catch (err) {
        console.error(err)
      }
      console.log(state.Dialog.DialogForm)
    },
    mutation__apps(state, value) {
      state.Apps = value
    },
  },
  actions: {
    ResetErrorMessage({ commit }) {
      commit('mutation__reset_error_message')
    },
    AUTH_API_USER({ commit }, value) {
      return new Promise((resolve, reject) => {
        axiosIns.get('pm/api/user/me/')
          .then(data => {
            commit('mutation__user', data.data)
            resolve(data)
          })
          .catch(err => {
            reject(err)
          })
      })
    },
    API_PREFERENCE({ commit }, value) {
      return new Promise((resolve, reject) => {
        axiosIns.get('pm/api/preference')
          .then(data => {
            commit('mutation__preference', data.data)
            resolve(data)
          })
          .catch(err => {
            reject(err)
          })
      })
    },
    API_APPS_LIST({ commit }, value) {
      return new Promise((resolve, reject) => {
        axiosIns.get('pm/api/forms/?fields=id,name')
          .then(data => {
            commit('mutation__apps', data.data)
            resolve(data)
          })
          .catch(err => {
            reject(err)
          })
      })
    },
    API({ commit }, value) {
      return new Promise((resolve, reject) => {
        axiosIns.get(`pm/api/${value}`)
          .then(data => {
            resolve(data)
          })
          .catch(err => {
            reject(err)
          })
      })
    },
    OpenDrawerOnClick({ commit }, value) {
      commit(value.DrawerMutation, {
        DrawerModel: true,
        DrawerShowAppBar: value.ShowAppBarOnDrawer,
        DrawerSize: value.DrawerSize,
        DrawerFormType: value.DrawerFormType,
        DrawerLoader: true,
        DrawerActionType: value.DrawerActionType,
        DrawerFormTitle: value.DrawerFormTitle,
        DrawerFormAPICall: value.DrawerFormAPICall,
        DrawerFormSubmit: value.DrawerFormSubmit,
        DrawerApiForm: value.DrawerApiForm,
        DrawerShowAction: value.DrawerShowAction,
        DrawerFilterForm: value.DrawerFilterForm,
        DrawerFilterStore: value.DrawerFilterStore,
        DrawerForm: [],
      })
      let endpoint = 'forms'
      let type = 'form_name'
      let addons_url = value.DrawerAddons ? value.DrawerAddons : 'addons/app/api/'
      if (value && value.DrawerFilterForm) {
        type = 'filter_name'
        endpoint = 'get_model_filter'
      }
      if (value && value.DrawerFormAPICall) {
        commit(value.DrawerMutation, { DrawerLoader: true, DrawerForm: [] })

        return new Promise((resolve, reject) => {
          axiosIns.get(
            `${addons_url}/${endpoint}/?${type}=${value.DrawerFormType}${
              value.DrawerExtraParam ? value.DrawerExtraParam : ''
            }`,
          )
            .then(data => {
              commit(value.DrawerMutation, {
                DrawerForm: data.data,
                DrawerLoader: false,
              })

              resolve(data)
            })
            .catch(err => {
              reject(err)
              commit(value.DrawerMutation, {
                DrawerForm: [],
                DrawerLoader: false,
              })
            })
        })
      }
      commit(value.DrawerMutation, {
        DrawerModel: true,
        DrawerShowAppBar: value.ShowAppBarOnDrawer,
        DrawerSize: value.DrawerSize,
        DrawerFormType: value.DrawerFormType,
        DrawerLoader: false,
      })
    },
    OpenFullDialogOnClick({ commit }, value) {
      commit('mutation__dialog', {
        FullDialog: true,
      })
    },

    OpenDialogOnClick({ commit }, value) {
      commit(value.DialogMutation, value)
      commit(value.DialogMutation, { DialogForm: [], Loader: true })
      if (value.API_FORM) {
        return new Promise((resolve, reject) => {
          axiosIns.get(
            `pm/api/forms/get_form/?form_name=${value.FormName}${value.DialogExtraParam ? value.DialogExtraParam : ''}`,
          )
            .then(data => {
              commit(value.DialogMutation, { DialogForm: data.data, Loader: false })
              resolve(data)
            })
            .catch(err => {
              reject(err)
              commit(value.DialogMutation, { DialogForm: [], Loader: false })
            })
        })
      }
      commit(value.DialogMutation, { Loader: false })
    },
    OpenConfirmationDialogOnClick({ commit }, value) {
      commit('mutation__confirmationdialog', value)
    },
    EnableDrawerLoader({ commit }) {
      commit('mutation__drawer', { DrawerLoader: true })
    },
    DisableDrawerLoader({ commit }) {
      commit('mutation__drawer', { DrawerLoader: false })
    },

    CloseDrawer({ commit }) {
      commit('mutation__drawer', { DrawerLoader: false, DrawerModel: false, DrawerForm: [] })
    },
    CloseSecondDrawer({ commit }) {
      commit('mutation__second_drawer', { DrawerModel: false, DrawerModel: false, DrawerForm: [] })
    },

    CloseDialog({ commit }) {
      commit('mutation__dialog', { Dialog: false, DialogWindow: 1, DialogSize: '400' })
    },
    DialogChangeWindow({ commit }, window) {
      commit('mutation__dialog', { DialogWindow: window })
    },
    DialogLoader({ commit }) {
      commit('mutation__dialog', { Loader: true })
    },
    DisableDialogLoader({ commit }) {
      commit('mutation__dialog', { Loader: false })
    },
    CloseConfirmationDialog({ commit }) {
      commit('mutation__confirmationdialog', { Dialog: false })
    },
    EnableConfirmationLoader({ commit }) {
      commit('mutation__confirmationdialog', { Loader: true })
    },
    DisableConfirmationLoader({ commit }) {
      commit('mutation__confirmationdialog', { Loader: false })
    },
    CloseNormalDialog({ commit }) {
      commit('mutation__dialog', { Dialog: false })
    },
    Snackbar({ commit }, message) {
      commit('mutation__snackbar', message)
    },
    CloseSnackbar({ commit }) {
      commit('mutation__snackbar', { bar: false })
    },

    // BusEvent({ commit }, value) {
    //   console.log(value)
    //   bus.$emit(value.custom_action)
    //   commit('mutation__confirmationdialog', { Dialog: false })

    // },
    GET_ADDONS({ commit }, query = '') {
      return new Promise((resolve, reject) => {
        axiosIns
          .get('/api/addons/' + query)
          .then(data => {
            resolve(data)
          })
          .catch(err => {
            reject(err)
          })
      })
    },
    POST_ADDONS({ commit }, payload) {
      console.log(payload.body)
      return new Promise((resolve, reject) => {
        axiosIns
          .post('/api/addons/' + payload.query, payload.body)
          .then(data => {
            resolve(data)
          })
          .catch(err => {
            reject(err)
          })
      })
    },
  },
  modules: {
    appConfig: appConfigStoreModule,
    app,
    ...dynamicModules,
    // Other Store

    UsersStore,
    TodoStore,
    ProjectStore,
    RepositoriesStore
  },
})