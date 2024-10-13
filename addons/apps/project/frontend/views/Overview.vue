<template>
  <div >
    <div class="project-details">
      <p><strong>Description:</strong> <span v-html="project.description"></span></p>
      <p><strong>Status:</strong> {{ project.status }}</p>
      <p><strong>Start Date:</strong> {{ formatDate(project.start_date) }}</p>
      <p><strong>End Date:</strong> {{ formatDate(project.end_date) }}</p>
      <p><strong>Owner:</strong> {{ project.owner }}</p>
    </div>
    <div class="project-stats">
      <h2>Project Statistics</h2>
      <ul>
        <li>Tasks Completed: {{ project.tasksCompleted }} / {{ project.totalTasks }}</li>
        <li>Budget Used: ${{ project.budgetUsed }} / ${{ project.totalBudget }}</li>
        <!-- <li>Team Members: {{ project.teamMembers.length }}</li> -->
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProjectOverview',
  data() {
    return {
      
    };
  },
  props: {
    project: {
      type: Object,
      required: true
    }
  },
  methods: {
    formatDate(date) {
      return new Date(date).toLocaleDateString();
    }
  }
};
</script>

<style scoped>
.project-overview {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
}

.project-details, .project-stats {
  margin-top: 20px;
}

h1 {
  color: #333;
}

h2 {
  color: #666;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 10px;
}
</style>
