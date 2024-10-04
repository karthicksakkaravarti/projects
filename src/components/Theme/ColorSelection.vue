<template>
  <div class="justify-start">
    <div class="pt-6">{{ title }}</div>

    <v-hover v-bind:key="id" v-for="(theme, id) in themes">
      <template v-slot:default="{ hover }">
        <v-card :disable="$vuetify.theme.dark" @click="SetSolidColor(theme)">
          <v-card-text class="ma-0 pa-2">
            
          </v-card-text>

          <v-fade-transition>
            <v-overlay
              opacity="0"
              v-if="
                hover ||
                ($vuetify.theme.themes.light.primary == theme.primary &&
                  $vuetify.theme.themes.light.secondary == theme.secondary)
              "
              absolute
            >
              <v-icon color="white">mdi-check-circle</v-icon>
            </v-overlay>
          </v-fade-transition>
        </v-card>
      </template>
    </v-hover>
  </div>
</template>

<script>
export default {
  props: {
    title: { deafult: "" },
    themes: {},
  },
  methods: {
    SetSolidColor(theme) {
      this.$vuetify.theme.themes.light.primary = theme.primary;
      this.$vuetify.theme.themes.light.secondary = theme.secondary;
    },
  },
};
</script>

<style scoped>
.halves-circle1 {
  background: rgb(20, 20, 20);
  height: var(--size);
  width: var(--size);
  border: var(--border) solid;
  border-radius: 100%;
  transform: rotate(45deg);
}

#hc2 {
  --size: 0px;
  --border: 18px;
}

#dot {
  --size: 0px;
  --border: 20px;
}
</style>