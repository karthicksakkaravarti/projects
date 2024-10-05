<template>
  <v-container>
    <h1>Create New Project</h1>
    <v-form ref="form" v-model="valid" @submit.prevent="submit">
      <v-text-field
        v-model="project.name"
        label="Project Name"
        :rules="[v => !!v || 'Name is required']"
        required
      ></v-text-field>

      <v-textarea
        v-model="project.description"
        label="Description"
        :rules="[v => !!v || 'Description is required']"
        required
      ></v-textarea>

      <v-menu
        ref="startDateMenu"
        v-model="startDateMenu"
        :close-on-content-click="false"
        :nudge-right="40"
        transition="scale-transition"
        offset-y
        min-width="290px"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            v-model="project.start_date"
            label="Start Date"
            prepend-icon="mdi-calendar"
            readonly
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker v-model="project.start_date" @input="startDateMenu = false"></v-date-picker>
      </v-menu>

      <v-menu
        ref="endDateMenu"
        v-model="endDateMenu"
        :close-on-content-click="false"
        :nudge-right="40"
        transition="scale-transition"
        offset-y
        min-width="290px"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-text-field
            v-model="project.end_date"
            label="End Date"
            prepend-icon="mdi-calendar"
            readonly
            v-bind="attrs"
            v-on="on"
          ></v-text-field>
        </template>
        <v-date-picker v-model="project.end_date" @input="endDateMenu = false"></v-date-picker>
      </v-menu>

      <v-select
        v-model="project.owner"
        :items="users"
        label="Owner"
        item-text="username"
        item-value="id"
        :rules="[v => !!v || 'Owner is required']"
        required
      ></v-select>

      <v-btn :disabled="!valid" color="success" type="submit">Create Project</v-btn>
    </v-form>
  </v-container>
</template>

<script>
import { mapActions } from 'vuex'
import axios from 'axios'

export default {
  name: 'ProjectCreate',
  data() {
    return {
      valid: false,
      startDateMenu: false,
      endDateMenu: false,
      project: {
        name: '',
        description: '',
        start_date: '',
        end_date: '',
        owner: null,
      },
      users: [],
    }
  },
  created() {
    this.fetchUsers()
  },
  methods: {
    ...mapActions('ProjectStore', ['CREATE_PROJECT']),
    fetchUsers() {
      axios.get('/api/users/') // Adjust the endpoint as necessary
        .then(response => {
          this.users = response.data
        })
        .catch(error => {
          console.error(error)
        })
    },
    submit() {
      this.CREATE_PROJECT(this.project)
        .then(() => {
          this.$router.push('/projects')
        })
        .catch(error => {
          console.error(error)
        })
    },
  },
}
</script>