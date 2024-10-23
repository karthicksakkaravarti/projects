const repositoriesRoutes = [
  {
    path: '/addons/apps/repositories',
    name: 'repositories',
    component: () => import('@/../addons/apps/repositories/frontend/views/RepositoriesList.vue'),

    meta: {
      layout: 'content',
    },

  },
  {
    path: '/addons/apps/repositories/:pid/files',
    name: 'repository-files',
    component: () => import('@/../addons/apps/repositories/frontend/views/RepositoryFiles.vue'),
    meta: {
      layout: 'content',
    },
  },
]

export default repositoriesRoutes
