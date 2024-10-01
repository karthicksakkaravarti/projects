const todoRoutes = [
  {
    path: '/addons/apps/todo',
    name: 'ToDO',
    component: () => import('@/../addons/apps/todo/frontend/views/Todo.vue'),

    meta: {
      layout: 'content',
    },
  },
]

export default todoRoutes
