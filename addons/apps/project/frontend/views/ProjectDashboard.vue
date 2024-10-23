<template>
  <div class="project-dashboard">
    <!-- New full-width header -->
    <v-card class="project-header mb-4" flat >
      <v-container fluid>
        <v-row align="center">
          <v-col cols="12" sm="6" md="4">
            <h1 class="text-h4 font-weight-bold">{{ project.name }}</h1>
            <v-chip :color="getStatusColor(project.status)" text-color="white" class="mt-2">
              {{ project.status }}
            </v-chip>
          </v-col>
          <v-col cols="12" sm="6" md="4">
            <v-list-item two-line>
              <v-list-item-icon>
                <v-icon color="primary">mdi-calendar-range</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-subtitle>Project Timeline</v-list-item-subtitle>
                <v-list-item-title class="text-h6">
                  {{ formatDate(project.start_date) }} - {{ formatDate(project.end_date) }}
                </v-list-item-title>
                <v-list-item-subtitle :class="{ 'red--text': getRemainingDays(project.end_date) < 10 }">
                  {{ getRemainingDays(project.end_date) }} days remaining
                </v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-col>
          <v-col cols="12" md="4">
            <v-list-item two-line>
              <v-list-item-icon>
                <v-icon color="primary">mdi-text-box-outline</v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-subtitle>Description</v-list-item-subtitle>
                <v-list-item-title v-html="project.description"></v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-col>
        </v-row>
        <v-tabs elevation="0" v-model="activeTab">
              <v-tab v-for="tab in tabs" :key="tab.value">
                <v-icon left>{{ tab.icon }}</v-icon>
                <span class="text-transform-capitalize">{{ tab.label }}</span>
              </v-tab>
            </v-tabs>

            <v-tabs-items v-model="activeTab">
              <v-tab-item v-for="tab in tabs" :key="tab.value">
                <v-card flat>
                  <v-card-text>
                    <component :is="tab.component" :project="project"></component>
                  </v-card-text>
                </v-card>
              </v-tab-item>
            </v-tabs-items>
      </v-container>
    </v-card>


  </div>
</template>

<script>
import { mapActions } from 'vuex';
import Overview from './Overview.vue';
import Documentation from './Documentation.vue';
import Tasks from './Tasks.vue';
import Code from './Code.vue';

export default {
  name: 'ProjectDashboard',
  data() {
    return {
      project: {
        name: '',
        description: '',
        startDate: '',
        status: ''
      },
      activeTab: null,
      tabs: [
        { label: 'Overview', value: 'overview', icon: 'mdi-view-dashboard', component: Overview },
        { label: 'Docs', value: 'documentation', icon: 'mdi-book-open-page-variant', component: Documentation },
        { label: 'Tasks', value: 'tasks', icon: 'mdi-checkbox-marked-outline', component: Tasks },
        { label: 'Code', value: 'code', icon: 'mdi-source-branch', component: Code },
        // { label: 'CI/CD', value: 'cicd', icon: 'mdi-rocket-launch', component: CiCd },
      ],
    }
  },
  mounted() {
    this.fetchProjectData()
  },
  methods: {
    ...mapActions('ProjectStore', ['GET_PROJECT']),
    getRemainingDays(endDate) {
      const end = new Date(endDate)
      const now = new Date()
      const diffTime = end.getTime() - now.getTime()
      const diffDays = Math.ceil(diffTime / (1000 * 3600 * 24))
      return diffDays
    },
    async fetchProjectData() {
      try {
        const projectId = this.$route.params.pid; // Assuming the project ID is in the route params
        const projectData = await this.GET_PROJECT(projectId);
        this.project = projectData.data;
      } catch (error) {
        console.error('Error fetching project data:', error);
        // Handle error (e.g., show error message to user)
      }
    },
    formatDate(dateString) {
      const options = { year: 'numeric', month: 'long', day: 'numeric' }
      return new Date(dateString).toLocaleDateString(undefined, options)
    },
    getStatusColor(status) {
      const statusColors = {
        'Not Started': 'grey',
        'In Progress': 'blue',
        'On Hold': 'orange',
        'Completed': 'green',
        'Cancelled': 'red'
      }
      return statusColors[status] || 'grey'
    }
  }
}
</script>
