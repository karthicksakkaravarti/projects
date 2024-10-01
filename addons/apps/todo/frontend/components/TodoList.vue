<template>
  <v-container style="max-width: 500px">
    <v-text-field
      v-model="newTask"
      label="What are you working on?"
      solo
      @keydown.enter="create"
    >
      <template v-slot:append>
        <v-fade-transition>
          <v-icon
            v-if="newTask"
            @click="create"
          >
            mdi-plus-circle
          </v-icon>
        </v-fade-transition>
      </template>
    </v-text-field>

    <h2 class="text-h4 success--text pl-4">
      Tasks:&nbsp;
      <v-fade-transition leave-absolute>
        <span :key="`tasks-${tasks.length}`">
          {{ tasks.length }}
        </span>
      </v-fade-transition>
    </h2>

    <v-divider class="mt-4"></v-divider>

    <v-row
      class="my-1"
      align="center"
    >
      <strong class="mx-4 info--text text--darken-2"> Remaining: {{ remainingTasks }} </strong>

      <v-divider vertical></v-divider>

      <strong class="mx-4 success--text text--darken-2"> Completed: {{ completedTasks }} </strong>

      <v-spacer></v-spacer>

      <v-progress-circular
        :value="progress"
        class="mr-2"
      ></v-progress-circular>
    </v-row>

    <v-divider class="mb-4"></v-divider>

    <v-card v-if="tasks.length > 0">
      <v-slide-y-transition
        class="py-0"
        group
        tag="v-list"
      >
        <template v-for="(task, i) in tasks">
          <v-divider
            v-if="i !== 0"
            :key="`${i}-divider`"
          ></v-divider>

          <v-list-item :key="`${i}-${task.text}`">
            <v-list-item-action>
              <v-checkbox
                v-model="task.done"
                :color="(task.done && 'grey') || 'primary'"
              >
                <template v-slot:label>
                  <div
                    :class="(task.done && 'grey--text') || 'primary--text'"
                    class="ml-4"
                    v-text="task.title"
                  ></div>
                </template>
              </v-checkbox>
            </v-list-item-action>

            <v-spacer></v-spacer>

            <v-scroll-x-transition>
              <v-icon
                v-if="task.done"
                color="success"
              >
                mdi-check
              </v-icon>
            </v-scroll-x-transition>

            <v-icon
              class="ml-2"
              color="error"
              @click="deleteTask(task)"
            >
              mdi-delete
            </v-icon>
          </v-list-item>
        </template>
      </v-slide-y-transition>
    </v-card>
  </v-container>
</template>

<script>
import store from '@/store'

export default {
  data: () => ({
    tasks: [

    ],
    newTask: null,
  }),

  computed: {
    completedTasks() {
      return this.tasks.filter(task => task.done).length
    },
    progress() {
      return (this.completedTasks / this.tasks.length) * 100
    },
    remainingTasks() {
      return this.tasks.length - this.completedTasks
    },
  },
  created() {
    this.fetchTasks()
  },
  methods: {
    fetchTasks() {
      store
        .dispatch('TodoStore/GET_TODO')
        .then(data => {
          this.tasks = data.data.results
        })
        .catch(err => {
          console.error(err)
        })
    },
    create() {
      store
        .dispatch('TodoStore/POST_TODO', { title: this.newTask, completed: false })
        .then(data => {
          this.tasks.push(data.data)
          this.newTask = null
        })
        .catch(err => {
          console.error(err)
        })
    },
    deleteTask(task) {
      store
        .dispatch('TodoStore/DELETE_TODO', task.id)
        .then(() => {
          this.tasks = this.tasks.filter(t => t.id !== task.id)
        })
        .catch(err => {
          console.error(err)
        })
    },
  },
}
</script>
