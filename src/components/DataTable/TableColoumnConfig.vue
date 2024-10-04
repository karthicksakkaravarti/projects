<template>
  <v-menu
    v-model="menu"
    content-class="my-menu"
    offset-y
    :close-on-content-click="false"
  >
    <template v-slot:activator="{ on, attrs }">
      <v-btn
        :icon="title ? false : true"
        v-bind="attrs"
        v-on="on"
      >
        <v-icon
          title="Customize Columns"
          small
          color="primary"
        >
          mdi-table-cog
        </v-icon>
        <span v-if="title">{{ title }}</span>
      </v-btn>
    </template>

    <v-card elevation="0">
      <v-card-title class="d-flex justify-space-between">
        <span>{{ title ? title : 'Fields' }}</span>

        <div class="d-flex justify-end">
          <v-btn
            small
            icon
            color="primary"
            @click="$emit('removeFields')"
          >
            <v-icon>mdi-refresh</v-icon>
          </v-btn>
        </div>
      </v-card-title>

      <v-divider></v-divider>

      <v-card-text class="ma-0 pa-3">
        <v-text-field
          v-model="search"
          prepend-inner-icon="mdi-magnify"
          dense
          hide-details
          placeholder="Search"
        ></v-text-field>
        <v-simple-table
          dense
          fixed-header
          class="mt-4"
          height="200px"
        >
          <template v-slot:default>
            <draggable
              tag="tbody"
              :list="FieldList"
            >
              <tr
                v-for="(field, key) in filteredItems"
                :key="key"
                @mouseover="c_index = field.text"
                @mouseleave="c_index = -1"
              >
                <td
                  class="justify-space-between pa-0 ma-0 d-flex"
                  style="width: 250px; cursor: move"
                >
                  <div>
                    <v-icon :color="c_index == field.text ? 'primary' : ''">
                      mdi-apps
                    </v-icon>
                    {{ field.text }}
                  </div>
                  <div></div>
                  <div>
                    <v-switch
                      v-model="field.is_default"
                      flat
                      dense
                      class="ma-0 pa-0"
                      :ripple="false"
                      hide-details
                    ></v-switch>
                  </div>
                </td>
              </tr>
            </draggable>
          </template>
        </v-simple-table>
      </v-card-text>
      <v-divider></v-divider>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          rounded
          small
          color="primary"
          @click="
            menu = false
            $emit('header_list', FieldList)
          "
        >
          Save
        </v-btn>
        <v-btn
          rounded
          small
          color="primary"
          @click="menu = false"
        >
          Close
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-menu>
</template>

<script>
import draggable from 'vuedraggable'

export default {
  components: {
    draggable,
  },
  props: {
    FieldList: [],
    title: { default: null },
  },

  data() {
    return {
      c_index: -1,
      menu: false,
      Field: [],
      search: '',
    }
  },

  computed: {
    filteredItems() {
      return this.FieldList.filter(item => item.text.toLowerCase().match(this.search))
    },
  },

  mounted() {
    // this.Field = Object.assign([], this.FieldList);
    // this.$emit("header_list", this.FieldList)
  },
}
</script>

<style>
</style>
