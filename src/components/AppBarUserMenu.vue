<template>
  <v-menu offset-y left nudge-bottom="14" min-width="230" content-class="user-profile-menu-content">
    <template v-slot:activator="{ on, attrs }">
      <v-badge bottom color="success" overlap offset-x="12" offset-y="12" class="ms-4" dot>
        <v-avatar size="40px" v-bind="attrs" color="primary" class="v-avatar-light-bg primary--text" v-on="on">
          <v-img v-if="$store.state.user.profile_picture" :src="$store.state.user.profile_picture"></v-img>

          <v-img v-else :src="require('')"></v-img>
        </v-avatar>
        <!-- <Avatar v-bind="attrs"
          v-on="on" :size="35" :ShowPicChange="false"> </Avatar> -->
      </v-badge>
    </template>
    <v-list>
      <div class="pb-3 pt-2">
        <v-badge bottom color="success" overlap offset-x="12" offset-y="12" class="ms-4" dot>
          <!-- <v-avatar
            size="40px"
            color="primary"
            class="v-avatar-light-bg primary--text"
          >
            <v-img :src="require('')"></v-img>
          </v-avatar> -->
          <Avatar :size="40" :ShowPicChange="false"> </Avatar>
        </v-badge>
        <div class="d-inline-flex flex-column justify-center ms-3" style="vertical-align: middle">
          <span class="text--primary mb-n1 mr-1">
            {{ $store.state.user.name }} ({{ $store.state.user.username }})
          </span>
          <small class="text--disabled text-capitalize"
            v-if="$store.state.user.user_master">
            {{ $store.state.user.user_master.title }}
          </small>
          <small class="text--disabled text-capitalize"
            v-if="$store.state.user.user_master">
            {{ $store.state.user.user_master.location }}
          </small>

        </div>
      </div>

      <v-divider></v-divider>
      <!-- Color -->
      <theme-color-selection />
      <v-divider></v-divider>

      <!-- Profile -->
      <!-- <v-list-item href="#">
        <v-list-item-icon class="me-2">
          <v-icon size="22">
            {{ icons.mdiAccountOutline }}
          </v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Profile</v-list-item-title>
        </v-list-item-content>
      </v-list-item> -->

      <!-- Settings -->
      <!-- <v-list-item href="#">
        <v-list-item-icon class="me-2">
          <v-icon size="22">
            {{ icons.mdiCogOutline }}
          </v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Settings</v-list-item-title>
        </v-list-item-content>
      </v-list-item> -->


      <!-- Prefile -->
      <v-list-item color="red" :to="{name: 'RM User View' , params: { id: $store.state.user.username }}">
        <v-list-item-icon class="me-2">
          <v-icon size="22">
            {{ icons.mdiAccount }}
          </v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>View Profile (Public)</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

       <!-- billing -->
       <v-list-item color="red" :to="{name: 'Timesheet My Work'}" href="#">
        <v-list-item-icon class="me-2">
          <v-icon size="22">
            {{ icons.mdiTimetable }}
          </v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>My Work</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <!-- Logout -->
      <v-list-item color="red" href="#">
        <v-list-item-icon class="me-2">
          <v-icon size="22">
            {{ icons.mdiLogoutVariant }}
          </v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Logout</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

          <!-- <v-btn color="primary" @click="navigate_route('mywork')" text x-small>My Work</v-btn> -->
    </v-list>
  </v-menu>
</template>

<script>
import {
  mdiAccountOutline,
  mdiEmailOutline,
  mdiCheckboxMarkedOutline,
  mdiChatOutline,
  mdiCogOutline,
  mdiCurrencyUsd,
  mdiHelpCircleOutline,
  mdiLogoutVariant,
  mdiAccount,
  mdiTimetable
} from '@mdi/js'

import ThemeColorSelection from '@core/layouts/components/app-customizer/ThemeColorSelection.vue'
import Avatar from '@/components/Users/Avatar.vue'

export default {
  components: {
    ThemeColorSelection,
    Avatar,
  },
  setup() {
    return {
      icons: {
        mdiAccountOutline,
        mdiEmailOutline,
        mdiCheckboxMarkedOutline,
        mdiChatOutline,
        mdiCogOutline,
        mdiCurrencyUsd,
        mdiHelpCircleOutline,
        mdiLogoutVariant,
        mdiAccount,
        mdiTimetable
      },
    }
  },
}
</script>

<style lang="scss">
.user-profile-menu-content {
  .v-list-item {
    min-height: 2.5rem !important;
  }
}
</style>
