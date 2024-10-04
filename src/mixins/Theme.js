import { mapGetters } from 'vuex'

export const Theme = {
  computed: {
    ...mapGetters('ThemeStore', ['Themes']),
  },
}
