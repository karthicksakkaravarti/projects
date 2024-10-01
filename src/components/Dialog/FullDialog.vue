<template>
    <v-dialog
      v-model="$store.state.Dialog.FullDialog"
      fullscreen
      hide-overlay
      transition="dialog-bottom-transition"
    >
      
      <v-card>
        <v-toolbar dense >
         
          <v-toolbar-title> <v-icon color="primary">mdi-hammer-screwdriver</v-icon> Setup</v-toolbar-title>
          <v-spacer></v-spacer>
          <v-toolbar-items>
             <v-btn icon  @click="$store.dispatch('CloseDialog')">
            <v-icon color="primary">mdi-close</v-icon>
          </v-btn>
          </v-toolbar-items>
        </v-toolbar>
      
      </v-card>
    </v-dialog>
</template>

<script>
export default {
  data() {
    return {
      notifications: false,
      sound: true,
      widgets: false,
    };
  },
};
</script>