import { mapGetters, mapActions } from 'vuex'

export const Users = {
  computed: {
    ...mapGetters('UsersStore', ['UsersList']),
    ComputedUsers: {
      get() {
        return this.field.value
      },
      set(newName) {
        // Setting Field
        this.field.value = newName
        return ''
      },
    },
    ComputedUserItems: {
      get() {    
        return this.UsersList
      },
      set(newName) {        
        return ''
      },
    },
  },

  methods: {
    ...mapActions('UsersStore', ['SetUsersList' , 'API_USERS', 'API_MASTER_USERS']),
  },
}
