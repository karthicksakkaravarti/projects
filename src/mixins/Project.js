import { mapGetters, mapActions } from 'vuex'

export const Project = {
  computed: {
    ...mapGetters('ProjectStore', ['Widgets']),
  },
  methods: {
    ...mapActions('ProjectStore', ['PROJECT_API_PROJECT', 'get_department','PROJECT_API_PROJECT_DELETE', 'PROJECT_API_PROJECT_POST', 'SetWidgets', 'PROJECT_API_GET_FINANCE_DATA', 'PROJECT_API_FINANCE_DELETE_DATA', 'PROJECT_API_FINANCE_DELETE_PATCH']),
  }
}
