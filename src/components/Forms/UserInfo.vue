<template>
  <div>
    <v-card elevation="0">
      <v-card-text>
        <div class="d-flex justify-space-between">
          <div>
            <v-btn color="primary" text small
              ><v-icon small>mdi-logout-variant</v-icon> Sign Out</v-btn
            >
          </div>
          <div><v-icon color="primary" @click="$store.dispatch('CloseDrawer')">mdi-close</v-icon></div>
        </div>
        <Info :AvatarSize="60" :ShowPicChange="true"> </Info>
      </v-card-text>
    </v-card>
    <v-divider></v-divider>
    <ThemeColorSelection />
    <v-divider></v-divider>
  </div>
</template>

<script>
import Info from "@/components/Users/Info.vue";
import ThemeColorSelection from "@/components/Theme/ThemeColorSelection.vue";

export default {
  components: {
    Info,
    ThemeColorSelection,
  },
};
</script>

<style>
</style>