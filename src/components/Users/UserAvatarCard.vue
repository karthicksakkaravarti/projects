<template>
  <div class="row" v-if="item[keyName]">
    <v-menu open-on-hover offset-x v-model="menu" :close-on-click="false"
      :close-on-content-click="false" nudge-width="30"
      transition="scale-transition">
      <template v-slot:activator="{ on }">
        <div class="d-flex"  v-on="on" @click="showProfile">
          <v-avatar class="ma-0 pa-0" size="28">
            <v-img v-if="item[profilePicture]" :src="item[profilePicture]"></v-img>
            <v-img v-else></v-img>
          </v-avatar>
          <div >
            <span class="ml-2 wrap-text" color="primary" >{{ item[keyName] }}</span>
          </div>
        </div>

      </template>
      <v-card :disabled="loader" width="350" height="190">
        <v-overlay :value="loader">
          <v-progress-circular indeterminate size="25"></v-progress-circular>
        </v-overlay>
        <v-list>
          <v-list-item>
            <v-list-item-avatar>
              <img v-if="item[profilePicture]" :src="item[profilePicture]" />
              <img v-else />
            </v-list-item-avatar>
            <v-list-item-content>
              <v-list-item-title>{{ item[keyName] }}</v-list-item-title>
              <v-list-item-subtitle>{{ details.email }} </v-list-item-subtitle>
            </v-list-item-content>
            <v-list-item-action>
              <v-btn icon @click="menu = false">
                <v-icon>mdi-close-circle</v-icon>
              </v-btn>
            </v-list-item-action>
          </v-list-item>
        </v-list>
        <div class="d-flex justify-start ma-2">
          <a :href="`MSTeams:/l/chat/0/0?users=${details.username}@gamil.com`">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
              <path fill="currentColor"
                d="M19.19 8.77q-.46 0-.86-.17q-.39-.17-.69-.47q-.3-.3-.47-.69q-.17-.4-.17-.86q0-.45.17-.85q.17-.4.47-.69q.3-.3.69-.47q.4-.18.86-.17q.45-.01.85.17q.4.17.7.47q.29.29.47.69q.17.4.17.85q0 .46-.17.86q-.17.39-.47.69q-.3.3-.7.47q-.4.17-.85.17m0-3.12q-.39 0-.69.27q-.25.27-.25.66t.25.67q.3.25.69.25q.39 0 .66-.25q.28-.25.28-.67q0-.39-.28-.66q-.27-.27-.66-.27M22 10.33V15q0 .63-.24 1.2q-.26.57-.67.99q-.43.43-1 .67q-.59.25-1.21.25q-.38 0-.76-.11q-.39-.07-.71-.25q-.24.79-.71 1.44q-.47.65-1.1 1.11q-.63.46-1.39.7q-.76.27-1.58.27q-.96 0-1.81-.33q-.82-.33-1.5-.94q-.66-.57-1.09-1.36q-.44-.8-.57-1.74H2.83q-.33 0-.59-.25q-.24-.24-.24-.58V7.73q0-.34.24-.59q.26-.24.59-.24H10q-.29-.6-.29-1.25q0-.61.23-1.15q.22-.5.62-.92q.4-.39.94-.62q.5-.23 1.12-.23q.61 0 1.14.23q.53.23.93.62q.4.42.62.92q.23.54.23 1.15q0 .6-.23 1.14q-.22.53-.62.92q-.4.4-.93.63q-.53.23-1.14.23q-.15 0-.31-.02q-.15-.02-.31-.05v.9h9.06q.39 0 .67.27q.27.27.27.66M12.63 4q-.35 0-.63.11q-.33.13-.56.36q-.22.23-.35.53q-.13.31-.13.65q0 .35.13.65q.13.3.35.53q.23.22.56.36q.28.13.63.13q.34 0 .64-.13q.3-.14.53-.36q.23-.23.36-.53q.14-.3.14-.65q0-.34-.14-.65q-.13-.3-.36-.53q-.23-.23-.53-.36q-.3-.11-.64-.11m-4.85 6.18h1.88V8.62H4.34v1.56h1.88v5h1.56m8.6 1.09v-5.62H12v5.42q0 .34-.24.58q-.26.25-.59.25H8.92q.13.67.47 1.25q.34.57.82.99q.48.41 1.1.65q.61.21 1.32.21q.77 0 1.45-.27q.68-.3 1.2-.81q.51-.51.8-1.19q.3-.68.3-1.46M20.75 15v-4.35h-3.12v5.71q.25.25.57.38q.3.12.68.12q.39 0 .73-.15q.34-.15.59-.4q.26-.25.4-.6q.15-.34.15-.71Z" />
            </svg></a>
          <a class="ml-2" :href="`mailto:${details.email}`"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24"
              viewBox="0 0 24 24">
              <path fill="currentColor"
                d="M8.56 12.03q0 .38-.06.73q-.11.34-.3.62q-.2.27-.49.43q-.3.16-.71.16q-.42 0-.71-.17t-.48-.45q-.19-.28-.27-.63q-.09-.35-.09-.72q0-.36.09-.72q.08-.35.27-.63t.5-.45q.3-.17.72-.17q.43 0 .72.17q.3.18.48.46q.18.29.27.64q.06.36.06.73M22 12v7.81q0 .39-.27.69q-.28.25-.67.25H7.94q-.39 0-.67-.25q-.27-.3-.27-.69V17H2.83q-.33 0-.59-.24Q2 16.5 2 16.17V7.83q0-.33.24-.59Q2.5 7 2.83 7h5.42V4.13q0-.37.25-.63q.26-.25.63-.25h10.74q.37 0 .63.25q.25.26.25.63v6.91l1.04.6h.01q.08.06.14.16q.06.09.06.2m-5-6.87v2.5h2.5v-2.5M17 8.88v2.5h2.5v-2.5M17 12.63v1.52l2.54-1.52m-6.91-7.5v2.5h3.12v-2.5m-3.12 3.75v2.5h3.12v-2.5m-3.12 3.75v1.69l2.01 1.24l1.11-.66v-2.27M9.5 5.13V7h1.77q.06 0 .11.04V5.12M7 15.32q.73 0 1.32-.26q.58-.26.99-.71q.4-.45.6-1.07q.21-.62.22-1.34q0-.69-.21-1.29q-.2-.59-.6-1.03q-.39-.44-.95-.69q-.57-.25-1.29-.25q-.77 0-1.37.25q-.59.25-1 .7q-.41.46-.62 1.08q-.21.63-.21 1.37q0 .7.21 1.3q.22.59.62 1.02q.4.43.97.68q.58.24 1.32.24m1.25 4.18h10.32L12 15.4v.77q0 .33-.24.59q-.26.24-.59.24H8.25m12.5 2.39v-6.03l-4.92 2.95Z" />
            </svg></a>
        </div>
        <v-divider></v-divider>
        <v-list>
          <v-list-item @click="showProfile">
            <v-list-item-action>
              <v-icon>mdi-account-circle</v-icon>
            </v-list-item-action>
            <v-list-item-subtitle>View full profile</v-list-item-subtitle>
          </v-list-item>
        </v-list>
      </v-card>
    </v-menu>



  </div>
  <div v-else>
    -
  </div>
</template>

<script>

export default {
  data() {
    return {
      menu: false,
      loader: false,
      details: {}
    }
  },
  props: {

    size: {
      default: 30
    },

    ShowMoreInfo: {
      type: Boolean,
      default: false
    },

    item: {
      type: Object
    },

    keyName: {
      type: String,
      default: ''
    },

    employeeKey: {
      type: String,
      default: 'employee_id'
    },

    profilePicture: {
      type: String,
      default: 'profile_picture'
    }
  },
  watch: {
    menu(value) {
      if (value) {
        this.getProfile()
      }
    }
  },
  methods: {
    getProfile() {
      this.loader = true
      var emp = null
      if (this.item[this.employeeKey]) {
        emp = this.item[this.employeeKey]
      } else if (this.item.employee_id) {
        emp = this.item.employee_id
      }

      this.$store
        .dispatch('API', 'users/' + emp + '/')
        .then(response => {
          this.loader = false
          this.details = response.data
        })
        .catch(error => {
          this.loader = false

        })
    },
    showProfile() {
      if (this.item[this.employeeKey]) {
        this.$router.push({ name: 'RM User View', params: { id: this.item[this.employeeKey] } })
      } else if (this.item.employee_id) {
        this.$router.push({ name: 'RM User View', params: { id: this.item.employee_id } })
      }
    }
  }

};
</script>

<style scoped>
.small-avatar {
  height: 10px;
  width: 10px;
}

.wrap-text {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
