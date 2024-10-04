import { mapGetters, mapActions } from 'vuex'

export const Milestones = {
  computed: {
    ...mapGetters('MilestonesStore', []),
  },
  methods: {
    ...mapActions('MilestonesStore', ['Milestones_API']),
  }
}
