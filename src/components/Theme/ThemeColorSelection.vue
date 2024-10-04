<template>
  <v-card elevation="0" class="pa-0 ma-0">
    <v-card-text>
      <div class="d-flex justify-space-between">
        <div>
          <b>Themes</b>
        </div>
         <v-switch class="pa-0 ma-0 pt-1 mb-1" @change="toggleTheme" inset dense hide-details label="Dark"></v-switch>
      </div>

      <ColorSelection  title="Solid" :themes="Themes.Solid"> </ColorSelection>
      <ColorSelection title="Light" :themes="Themes.Light"> </ColorSelection>
    </v-card-text>
  </v-card>
</template>

<script>
import { Theme } from "@/mixins/Theme";
import ColorSelection from "./ColorSelection.vue";
export default {
  mixins: [Theme],
  components: {
    ColorSelection,
  },
  methods: {
    toggleTheme() {
      this.$vuetify.theme.themes.light.primary == '#ff6400'
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
    }
  }
};
</script>

