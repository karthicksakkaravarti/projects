<template>
 
    <view-list
      :options="{
        store_action_name: 'ProjectStore/GET_PROJECTS',
        filter_table: 'projects',
      }"
      type="projects"
    >
    <template v-slot:top-right>
        <Button
        class="mt-0"
            :outlined="true"
            :rounded="true"
            mdi_icon="mdi-plus"
            click="OpenDrawerOnClick"
            title="Create Project"
            tooltip="Create Project"
            :options="{
              ShowAppBarOnDrawer: true,
              DrawerSize: '30%',
              DrawerFormType: 'projects',
              DrawerFormTitle: 'Create Project',
              DrawerAddons: 'addons/apps/project/api/projects',
              DrawerFormAPICall: true,
              DrawerFilterForm: false,
              DrawerMutation: 'mutation__drawer',
              DrawerActionType: 'new',
              DrawerFormSubmit: {
                btn_name: 'Create Project',
                store_action_name: 'ProjectStore/CREATE_PROJECT',
                custom_action: '',
                data: '',
              },
            }"
          />
    </template>
    </view-list>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import { ModuleImport } from '@/mixins/ModuleImport'
import { bus } from '@/main'
export default {
  mixins: [ModuleImport],
  name: 'ProjectList',
  data() {
    return {
      headers: [
        { text: 'ID', value: 'id' },
        { text: 'Name', value: 'name' },
        { text: 'Description', value: 'description' },
        { text: 'Start Date', value: 'start_date' },
        { text: 'End Date', value: 'end_date' },
        { text: 'Actions', value: 'actions', sortable: false },
      ],
    }
  },
  computed: {
    ...mapGetters('ProjectStore', ['allProjects']),
    projects() {
      return this.allProjects
    },
  },
  created() {
    this.GET_PROJECTS()
    bus.$on('form_success', (response, form_name, form_type = null) => {
        console.log(response, form_name, form_type)
        this.$store.dispatch('CloseDrawer')

      this.GET_PROJECTS()
    })
  },
  methods: {
    ...mapActions('ProjectStore', ['GET_PROJECTS']),
    viewProject(id) {
      // Navigate to a detailed view if implemented
      // For now, you can implement a modal or another view
      alert(`View details for project ID: ${id}`)
    },
  },
}
</script>