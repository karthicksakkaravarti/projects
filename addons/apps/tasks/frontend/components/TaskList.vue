<template>
    <v-container>
       
        <view-list project_relation="project" :options="{
    store_action_name: 'TasksStore/GET_TASKS',
    filter_table: 'tasks',
  }" type="tasks">
    <template v-slot:top-right>
        <Button class="mt-0 mr-2" :outlined="true" :rounded="true" mdi_icon="mdi-plus" click="OpenDrawerOnClick"
            title="Create " tooltip="Create" :options="{
                ShowAppBarOnDrawer: true,
                DrawerSize: '30%',
                DrawerFormType: 'tasks',
                DrawerFormTitle: 'Create',
                DrawerAddons: '/addons/apps/tasks/api/tasks',
                DrawerFormAPICall: true,
                DrawerFilterForm: false,
                DrawerMutation: 'mutation__drawer',
                DrawerExtraParam: `&project=${pid ? pid: ''}`,
                DrawerActionType: 'new',
                DrawerFormSubmit: {
                    btn_name: 'Create Task',
                    store_action_name: 'TasksStore/CREATE_TASK',
                    custom_action: '',
                    data: '',
                },
            }" />
    </template>
    <template #item-title="{ item }">
      <span>{{ item.title }}</span>
    </template>
    <template #item-status="{ item }">
      <span><v-chip small>{{ item.status }}</v-chip></span>
    </template>
    <template #item-description="{ item }">
      <span v-html="item.description"></span>
    </template>
    <template #item-created_by="{ item }">
      <span>{{ item.created_by.email }}</span>
    </template>
  </view-list>

    </v-container>
</template>

<script>
import store from '@/store'
import { ModuleImport } from '@/mixins/ModuleImport'
import { bus } from '@/main'
export default {

    mixins: [ModuleImport],
    data() {
        return {
            headers: [
                { text: 'Title', value: 'title' },
                { text: 'Status', value: 'status' },
                { text: 'Due Date', value: 'due_date' },
                { text: 'Actions', value: 'actions', sortable: false }
            ],
            tasks: []
        }
    },
    props: {
        pid: {
            type: String,
            required: false
        }
    },
    methods: {
        fetchTasks() {
            store.dispatch('TasksStore/GET_TASKS')
                .then(response => {
                    this.tasks = response.data.results
                })
                .catch(error => {
                    console.error(error)
                })
        },
        openCreateTask() {
            this.$router.push({ name: 'createTask' })  // You can define a route for creating tasks
        },
        viewTask(id) {
            this.$router.push({ name: 'taskView', params: { id } })
        },
        deleteTask(id) {
            if (confirm('Are you sure you want to delete this task?')) {
                store.dispatch('TasksStore/DELETE_TASK', id)
                    .then(() => this.fetchTasks())
                    .catch(error => console.error(error))
            }
        }
    },
    created() {
        this.fetchTasks()
    }
}
</script>