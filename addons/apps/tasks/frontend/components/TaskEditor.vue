<template>
    <v-form @submit.prevent="saveTask" v-if="task && task.id">
        <v-text-field v-model="task.title" label="Title" required></v-text-field>
        <v-textarea v-model="task.description" label="Description" required></v-textarea>
        <v-select
            v-model="task.status"
            :items="statusOptions"
            label="Status"
            required
        ></v-select>
        <v-menu
            ref="dueDateMenu"
            v-model="dueDateMenu"
            :close-on-content-click="false"
            transition="scale-transition"
            offset-y
            min-width="290px"
        >
            <template v-slot:activator="{ on, attrs }">
                <v-text-field
                    v-model="task.due_date"
                    label="Due Date"
                    readonly
                    v-bind="attrs"
                    v-on="on"
                ></v-text-field>
            </template>
            <v-date-picker v-model="task.due_date" @input="dueDateMenu = false"></v-date-picker>
        </v-menu>
        <v-btn type="submit" color="success">Save Task</v-btn>
    </v-form>
</template>

<script>
import store from '@/store'

export default {
    props: {
        taskID: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            task: {},
            statusOptions: ['pending', 'in_progress', 'completed'],
            dueDateMenu: false
        }
    },
    methods: {
        async getTask() {
            try {
                const response = await store.dispatch('TasksStore/GET_TASK', this.taskID)
                this.task = response.data
            } catch (error) {
                console.error(error)
            }
        },
        async saveTask() {
            try {
                await store.dispatch('TasksStore/PATCH_TASK', {
                    id: this.taskID,
                    data: this.task
                })
                this.$router.push({ name: 'tasks' })
                this.$emit('task-saved')
            } catch (error) {
                console.error('Error saving task:', error)
            }
        }
    },
    created() {
        this.getTask()
    }
}
</script>