<template>

  <view-list :options="{
    store_action_name: 'RepositoriesStore/GET_repositories',
    filter_table: 'repositories',
  }" type="repositories">
    <template v-slot:top-right>
      <Button class="mt-0" :outlined="true" :rounded="true" mdi_icon="mdi-plus" click="OpenDrawerOnClick"
        title="Create Repo" tooltip="Create Repo" :options="{
          ShowAppBarOnDrawer: true,
          DrawerSize: '30%',
          DrawerFormType: 'repo_form',
          DrawerFormTitle: 'Create Repo',
          DrawerAddons: '/addons/apps/repositories/api/repositories',
          DrawerFormAPICall: true,
          DrawerFilterForm: false,
          DrawerMutation: 'mutation__drawer',
          DrawerActionType: 'new',
          DrawerFormSubmit: {
            btn_name: 'Create Repo',
            store_action_name: 'RepositoriesStore/CREATE_repositories',
            custom_action: '',
            data: '',
          },
        }" />
    </template>
    <template #item-name="{ item }">
      <span>{{ item.name }}</span>
    </template>
    <template #item-status="{ item }">
      <span><v-chip small>{{ item.status }}</v-chip></span>
    </template>
    <template #item-description="{ item }">
      <span v-html="item.description"></span>
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

    }
  },
  computed: {
    ...mapGetters('RepositoriesStore', ['allProjects']),
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
    ...mapActions('RepositoriesStore', ['GET_PROJECTS']),
    viewProject(id) {
      // Navigate to a detailed view if implemented
      // For now, you can implement a modal or another view
      alert(`View details for project ID: ${id}`)
    },
  },
}
</script>