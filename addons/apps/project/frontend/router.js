const projectRoutes = [
  {
    path: '/addons/apps/project',
    name: 'Project',
    component: () => import('@/../addons/apps/project/frontend/views/ProjectList.vue'),

    meta: {
      layout: 'content',
    },
  },
]

export default projectRoutes
