<template>
    <v-container>
        <TaskEditor :taskID="taskID" />
    </v-container>
</template>

<script>
import TaskEditor from '../components/TaskEditor.vue'

export default {
    name: 'TaskView',
    components: {
        TaskEditor
    },
    data() {
        return {
            taskID: null
        }
    },
    created() {
        this.taskID = this.$route.params.id
    }
}
</script>