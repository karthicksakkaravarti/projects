<template>
  <div class="text-center ma-2">
    <v-snackbar rounded="pill"
 :value="true" dense :color="$store.state.Snackbar.color" outlined app text top right
      v-model="$store.state.Snackbar.bar">
 
      {{ $store.state.Snackbar.text }}

      <template v-slot:action="{ attrs }">
        <v-btn dense icon v-bind="attrs" @click="$store.dispatch('CloseSnackbar')">
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script>
export default {}
</script>

