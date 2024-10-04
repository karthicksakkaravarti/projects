<template>
  <app-card-actions @refresh="refetchData">
    <template slot="title" class="text-caption"><v-icon color="primary">mdi-drag-vertical</v-icon> {{ title }}
    </template>
    <template slot="before-actions">
      <v-chip v-if="show_chip && items" class="v-chip-light-bg primary--text me-3" color="primary" small>
        {{ getCount(items) }} Pending</v-chip>
    </template>
    <v-card-text>
      <v-simple-table v-if="['mywork', 'task'].includes($props.type)" dense fixed-header :height="height">
        <template v-slot:default>
          <v-list dense>
            <template v-for="(item, index) in items.results">
              <v-list-item @click="generate_route(item)" :key="item.title">
                <template v-slot:default="{ active }">
                  <!-- If Project -->
                  <template v-if="item.type == 'project'">
                    <v-list-item-content>
                      <v-list-item-title class="text-capitalize">
                        <a @click="generate_route(item, type = 'project', mode = 'view')">
                          <b>{{ item.name }}</b>({{ item.type }})
                        </a>
                      </v-list-item-title>
                      <v-list-item-subtitle class="d-flex">
                           {{ item.status }}
                      </v-list-item-subtitle>
                      <v-list-item-subtitle class="d-flex">

                        <span class="mt-1">Submitter:</span>
                        <user-avatar-card class="pa-1" :item="item.submitter" keyName="full_name" />
                        <!-- {{ item.submitter }} -->
                      </v-list-item-subtitle>
                      

                    </v-list-item-content>

                    <v-list-item-action>
                      <!-- <v-btn x-small text color="primary text-capitalize" @click="generate_route(item,type='project', mode='view')"> View</v-btn> -->
                      <v-btn x-small text color="primary text-capitalize" @click="generate_route(item)"> Approve</v-btn>
                    </v-list-item-action>
                  </template>
                  <!-- If CR -->
                  <template v-if="item.type == 'change request'">
                    <v-list-item-content>
                      <v-list-item-title class="text-capitalize">
                        <b>{{ item.reason }}</b>({{ item.type }})</v-list-item-title>

                      <v-list-item-subtitle class="d-flex">
                        ID : {{ item.id }}
                        <v-divider class="ma-1" vertical></v-divider>
                        Status: {{ item.status }}
                        <v-divider class="ma-1" vertical></v-divider>
                        Submitter: {{ item.submitter }}
                      </v-list-item-subtitle>
                    </v-list-item-content>

                    <v-list-item-action>
                      <div class="d-flex inline">
                        <v-btn x-small text color="primary text-capitalize"
                          @click="generate_cr_route(item)">Approve/Reject</v-btn>
                      </div>
                    </v-list-item-action>
                  </template>
                  <!-- Task -->
                  <template v-if="$props.type == 'task'">
                    <v-list-item dense @click="" :key="item.task_id" :value="item.id">

                      <template v-slot:default="{ active }">
                        <v-list-item-avatar>
                          <v-icon color="blue">mdi-checkbox-marked</v-icon>
                        </v-list-item-avatar>
                        <v-list-item-content>
                          <v-list-item-title class="primary--text">{{ item.task_id
                          }}</v-list-item-title>

                          <v-list-item-subtitle class="text--primary" v-text="item.title"></v-list-item-subtitle>

                          <v-list-item-subtitle v-text="item.subtitle"></v-list-item-subtitle>
                        </v-list-item-content>

                        <v-list-item-action>
                          <v-list-item-action-text v-text="item.action"></v-list-item-action-text>

                          <!-- <v-icon v-if="!active" color="grey lighten-1">
                            mdi-star-outline
                        </v-icon> -->

                          <!-- <v-icon v-else color="yellow darken-3">
                            mdi-star
                        </v-icon> -->
                        </v-list-item-action>
                      </template>
                    </v-list-item>

                    <v-list-item-action>
                      <div class="d-flex inline">
                        <v-btn x-small text color="primary text-capitalize" @click="generate_cr_route(item)">View</v-btn>
                      </div>
                    </v-list-item-action>
                  </template>

                </template>
              </v-list-item>

              <v-divider v-if="index < items.length - 1" :key="index"></v-divider>
            </template>
          </v-list>
        </template>
      </v-simple-table>

      <!-- WorkLog -->
      <template v-if="$props.type == 'timesheet'">
        <TimesheetEntry whosee="myWork"></TimesheetEntry>
      </template>
    </v-card-text>
  </app-card-actions>
</template>

<script>
import AppCardActions from '@core/components/app-card-actions/AppCardActions.vue'
import UserAvatarCard from '@/components/Users/UserAvatarCard.vue'
import TimesheetEntry from '@/apps/timesheet/components/TimesheetEntry.vue'

import store from '@/store'
import { ref, onUnmounted } from '@vue/composition-api'

import { Helper } from '@/mixins/Helper'

export default {
  mixins: [Helper],
  components: {
    AppCardActions,
    UserAvatarCard,
    TimesheetEntry
  },
  mounted() {
    this.refetchData()
  },
  props: {
    title: { default: 'Default' },
    api: { default: '' },
    show_chip: { default: false },
    type: {},
    height: {default: '300px'}
  },
  setup(props) {
    const items = ref([])
    const getCount = item => {
      if (props.type == 'mywork') { return item.overall_total }
      if (props.type == 'task') { return item.total_count }

    }
    const refetchData = hideOveraly => {
      store.dispatch('API', props.api).then(data => {
        items.value = data.data

        try {
          hideOveraly()
        } catch (_) { }
      })
    }

    return {
      refetchData,
      items,
      getCount
    }
  },
}
</script>
