const documentsRoutes = [
  {
    path: '/addons/apps/documents',
    name: 'documents',
    component: () => import('@/../addons/apps/documents/frontend/views/Documents.vue'),
    meta: {
      layout: 'content',
    },
  },
  // View Document
  {
    path: '/addons/apps/documents/:id',
    name: 'document',
    component: () => import('@/../addons/apps/documents/frontend/views/DocumentView.vue'),
    meta: {
      layout: 'content',
    },
  },
]

export default documentsRoutes
