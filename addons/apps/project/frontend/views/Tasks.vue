<template>
  <div>
    <component :is="DocumentsComponent" :pid="pid" />
  </div>
</template>

<script>
import { defineComponent, defineAsyncComponent, ref, computed } from '@vue/composition-api'

export default defineComponent({
  name: 'Documentation',
  setup(props, { root }) {
    const documentComponentLoaded = ref(false)

    const pid = computed(() => root.$route.params.pid)

    const DocumentsComponent = defineAsyncComponent(() => 
      import('@/../addons/apps/tasks/frontend/components/TaskList.vue')
        .then(module => {
          documentComponentLoaded.value = true
          return module
        })
        .catch(() => {
          documentComponentLoaded.value = false
          return { template: '<div>Documents component not found</div>' }
        })
    )

    return {
      DocumentsComponent,
      documentComponentLoaded,
      pid
    }
  }
})
</script>
