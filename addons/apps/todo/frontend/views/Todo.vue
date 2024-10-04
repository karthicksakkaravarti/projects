<!-- src/App.vue -->
<template>
  <v-app>
    <TodoList />
  </v-app>
</template>

<script>
import TodoList from '../components/TodoList.vue'

export default {
  components: {
    TodoList,
  },
}
</script>
