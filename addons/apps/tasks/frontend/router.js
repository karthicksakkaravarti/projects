import TaskList from '@/../addons/apps/tasks/frontend/components/TaskList.vue'
import TaskView from '@/../addons/apps/tasks/frontend/views/TaskView.vue'

const tasksRoutes = [
    {
        path: '/tasks',
        name: 'tasks',
        component: TaskList,
        meta: {
            layout: 'content',
        },
    },
    {
        path: '/tasks/:id',
        name: 'taskView',
        component: TaskView,
        meta: {
            layout: 'content',
        },
    },
]

export default tasksRoutes