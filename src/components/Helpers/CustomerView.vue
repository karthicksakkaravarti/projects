<template>
  <div class="d-flex">
    <!-- <v-avatar :class="`v-avatar-light-bg primary--text`" size="30">
      <span class="font-weight-medium">{{ customer.contact_person_name.slice(0, 2).toUpperCase() }}</span>
    </v-avatar> -->
    <div class="d-flex flex-column ms-3">
      <span class="d-block text--primary text-truncate">
        {{ customer.name }} {{ customer.number ? `(${customer.number})` : '' }} 
      </span>
      <!-- <span class="text-xs"></span> -->
    </div>
  </div>
</template>

<script>
export default {
  props: {
    customer: { default: {} },
  },
  mounted() {
  },
}
</script>

<style>
</style>