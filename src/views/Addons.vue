<template>
  <v-card elevation="0">
    <v-card-text>
      <v-row>
        <v-col
          cols="12"
          sm="2"
        >
          <b>CATEGORIES</b>
          <v-list>
            <v-divider></v-divider>
            <v-list
              nav
              dense
            >
              <v-list-item-group
                v-model="selectedItem"
                color="primary"
              >
                <v-list-item
                  v-for="(item, i) in items"
                  :key="i"
                >
                  <v-list-item-content>
                    <v-list-item-title>{{ item.text }}</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list-item-group>
            </v-list>
          </v-list>
        </v-col>
        <v-col
          cols="12"
          sm="10"
        >
          <view-list
            :options="{
              store_action_name: 'GET_ADDONS',
              filter_table: 'appsInstaller',
            }"
            type="appsInstaller"
          >
            <template #item-is_installed="{ item }">
              <v-chip x-small>
                {{ item.is_installed ? 'Installed' : 'Not Installed' }}
              </v-chip>
            </template>
            <template #item-app_name="{ item }">
              <span
                class="text-capitalize"
              ><v-avatar
                 color="primary"
                 class="white--text"
                 size="30"
               >{{ item.app_name[0] }}</v-avatar>
                {{ item.app_name }}
              </span>
            </template>
            <template #item-actions="{ item }">
              <v-btn
                v-if="!item.is_installed"
                x-small
                color="primary"
                @click="installAddons(item.app_name)"
              >
                Install
              </v-btn>
            </template>
          </view-list>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>

<script>
import { ModuleImport } from '@/mixins/ModuleImport'
import store from '@/store'

export default {
  mixins: [ModuleImport],

  setup() {
    const items = [
      { text: 'ALL' },
      { text: 'Sales' },
      { text: 'Services' },
      { text: 'Accounting' },
      { text: 'Inventory' },
      { text: 'Manufacturing' },
      { text: 'Website' },
      { text: 'Marketing' },
      { text: 'Human Resources' },
      { text: 'Productive' },
      { text: 'Administration' },
    ]
    const selectedItem = 0
    const search = ''

    function installAddons(addonName) {
      store.dispatch('POST_ADDONS', { query: 'install/', body: { app_name: addonName } }).then(data => {
        // Check if the data indicates success, if needed
        // if (data.success) {
        window.location.reload()

        // }
      })
    }

    return {
      items,
      selectedItem,
      search,

      // Func
      installAddons,
    }
  },
}
</script>

<style>
</style>
