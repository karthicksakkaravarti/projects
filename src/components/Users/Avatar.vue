<template>
  <v-hover>
    <template v-slot:default="{ hover }">
      <v-avatar
        class="ml-2"
        :style="`${ShowMoreInfo ? 'cursor:pointer' : ''}`"
        @click="call"
        :size="size"
      >
        <img v-if="$store.state.user.profile_picture" :src="$store.state.user.profile_picture" />

        <img v-else  />

        <v-fade-transition>
          <v-overlay v-if="hover && ShowPicChange" absolute color="primary">
            <v-btn icon><v-icon>mdi-camera-enhance-outline</v-icon></v-btn>
          </v-overlay>
        </v-fade-transition>
      </v-avatar>
    </template>
  </v-hover>
</template>

<script>
export default {
  props: {
    size: { default: 30 },
    ShowMoreInfo: { default: false, type: Boolean },
    ShowPicChange: { default: false, type: Boolean },
  },
  methods: {
    call() {
      if (this.ShowMoreInfo) {
        this.$store.dispatch("OpenDrawerOnClick", {
          ShowAppBarOnDrawer: false,
          DrawerSize: "28%",
          DrawerFormType: "UserInfo",
        });
      }
    },
  },
};
</script>

<style>
</style>
