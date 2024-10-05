<template>
  <v-data-table
    v-model="selected"
    class="user-search me-3 mb-4 row-pointer"
    :headers="generate_headers"
    :loading="loader"
    :show-select="show_select"
    :options.sync="table_pagination"
    :server-items-length="items.count"
    :items="items.results"
    :row-class="customRowClass"
    @click:row="handleClick"
  >
    <template v-slot:header.data-table-select="{ on, props }">
      <TableColoumnConfig
        table-coloumn-config
        :field-list="headers"
        @header_list="set_header"
        @removeFields="removeFields"
      ></TableColoumnConfig>
    </template>
    <template v-slot:progress>
      <v-overlay :value="true">
        <v-progress-circular
          indeterminate
          size="64"
        ></v-progress-circular>
      </v-overlay>
    </template>
    <template v-slot:item.data-table-select="{ isSelected, select, item }">
      <div class="d-flex justify-around">
        <slot
          name="item-data-table-select"
          :item="item"
          class="mr-2"
        >
        </slot>
        <v-simple-checkbox
          v-if="show_select_checkbox"
          class="ml-2"
          color="primary"
          :value="isSelected"
          @input="select($event)"
        ></v-simple-checkbox>
      </div>
    </template>
    <template v-slot:top>
      <v-toolbar
        flat
        color="white"
      >
        <v-toolbar-title>
          <b>{{ title }}</b>
        </v-toolbar-title>
        <div
          v-if="showFilter"
          class="ml-2 mt-0"
        >
          <BaseButton
            :outlined="true"
            :rounded="true"
            mdi_icon="mdi-filter"
            click="OpenDrawerOnClick"
            :title="getFilterCount() > 0 ? `(${getFilterCount()}) Filter Applied` : 'Filter'"
            tooltip="Apply Filter"
            :options="{
              ShowAppBarOnDrawer: true,
              DrawerSize: '30%',
              DrawerFormType: options.filter_table,
              DrawerExtraParam: generateExtraParams(),
              DrawerFormTitle: getFilterCount() > 0 ? `(${getFilterCount()}) Filter Applied` : 'Filter',
              DrawerFormAPICall: true,
              DrawerFilterForm: true,
              DrawerMutation: 'mutation__drawer',
              DrawerActionType: 'new',
              DrawerFormSubmit: {
                btn_name: 'Apply',
                store_action_name: options.store_action_name,
                custom_action: options.custom_action ? options.custom_action : '',
                data: getFilterCount() > 0 ? `(${getFilterCount()}) Filter Applied` : '',
              },
            }"
          />
        </div>
        <div v-else>
          <slot name="filter-space"></slot>
        </div>
        <v-spacer></v-spacer>
        
        <v-card-title
          small
          class="ma-0 pa-0"
        >
          <v-text-field
            v-model="search_text"
            v-debounce:1000="search"
            rounded
            filled
            dense
            class="mt-4"
            prepend-inner-icon="mdi-magnify"
            label="Search"
            single-line
            clearable
          ></v-text-field>
          <v-btn class="mb-3" icon small @click="get_list"><v-icon>mdi-refresh</v-icon></v-btn>
          <slot name="top-right">
          <b>hellow</b>
        </slot>
        </v-card-title>
        
      </v-toolbar>
    </template>

    <template v-slot:item.id="{ item }">
      <slot
        name="item-id"
        :item="item"
      >
      </slot>
    </template>
    <template v-slot:item.is_installed="{ item }">
      <slot
        name="item-is_installed"
        :item="item"
      >
      </slot>
    </template>
    <template v-slot:item.app_name="{ item }">
      <slot
        name="item-app_name"
        :item="item"
      >
      </slot>
    </template>
    <template v-slot:item.project_key="{ item }">
      <slot
        name="item-project_key"
        :item="item"
      >
      </slot>
    </template>
    <template v-slot:item.title="{ item }">
      <slot
        name="item-title"
        :item="item"
      >
      </slot>
    </template>
    <template v-slot:item.invoice_number="{ item }">
      <slot
        name="item-invoice_number"
        :item="item"
      >
      </slot>
    </template>
    <template v-slot:item.work_week="{ item }">
      <slot
        name="item-work_week"
        :item="item"
      >
      </slot>
    </template>
    <template v-slot:item.status="{ item }">
      <slot
        name="item-status"
        :item="item"
      >
      </slot>
    </template>
    <template v-slot:item.name="{ item }">
      <slot
        name="item-name"
        :item="item"
      >
      </slot>
    </template>
    <template v-slot:item.state="{ item }">
      <slot
        name="item-state"
        :item="item"
      >
      </slot>
    </template>
    <template v-slot:item.milestone_type="{ item }">
      <slot
        name="item-milestone-type"
        :item="item"
      >
      </slot>
    </template>
    <template v-slot:item.impacted_milestone="{ item }">
      <slot
        name="item-impacted-milestone"
        :item="item"
      >
      </slot>
    </template>
    <template v-slot:item.payment_delivery_status="{ item }">
      <slot
        name="item-payment-delivery-status"
        :item="item"
      >
      </slot>
    </template>
    <template v-slot:item.cr="{ item }">
      <slot
        name="item-cr"
        :item="item"
      >
      </slot>
    </template>
    <template v-slot:item.milestones="{ item }">
      <slot
        name="item-milestones"
        :item="item"
      >
      </slot>
    </template>
    <template v-slot:item.dependencies="{ item }">
      <slot
        name="item-dependencies"
        :item="item"
      >
      </slot>
    </template>
    <template v-slot:item.risk="{ item }">
      <slot
        name="item-risk"
        :item="item"
      >
      </slot>
    </template>
    <template v-slot:item.customer="{ item }">
      <slot
        name="item-customer"
        :item="item"
      >
      </slot>
    </template>
    <template v-slot:item.CRDetail="{ item }">
      <slot
        name="item-CRDetail"
        :item="item"
      >
      </slot>
    </template>
    <template v-slot:item.team="{ item }">
      <slot
        name="item-team"
        :item="item"
      >
      </slot>
    </template>
    <template v-slot:item.actions="{ item }">
      <slot
        name="item-actions"
        :item="item"
      >
      </slot>
    </template>

    <template v-slot:item.availability="{ item }">
      <slot
        name="item-availability"
        :item="item"
      >
      </slot>
    </template>
    <template v-slot:item.notification_metrix="{ item }">
      <slot
        name="item-notification_metrix"
        :item="item"
      >
      </slot>
    </template>
    <template v-slot:item.assert_id="{ item }">
      <slot
        name="item-assert_id"
        :item="item"
      >
      </slot>
    </template>
    <template v-slot:item.assignee="{ item }">
      <slot
        name="item-assignee"
        :item="item"
      >
      </slot>
    </template>

    <template v-slot:item.title="{ item }">
      <slot
        name="item-title"
        :item="item"
      >
      </slot>
    </template>

    <template v-slot:item.hours="{ item }">
      <slot
        name="item-hours"
        :item="item"
      >
      </slot>
    </template>

    <template v-slot:item.resource_name="{ item }">
      <slot
        name="item-resource_name"
        :item="item"
      >
        <user-avatar-card
          :item="item"
          key-name="resource_name"
        />
      </slot>
    </template>

    <template v-slot:item.responsible="{ item }">
      <slot
        name="item-responsible"
        :item="item"
      >
        <user-avatar-card
          :item="item.owner"
          key-name="full_name"
        />
      </slot>
    </template>

    <template v-slot:item.owner="{ item }">
      <slot
        name="item-owner"
        :item="item"
      >
        <user-avatar-card
          :item="item.owner"
          key-name="full_name"
        />
      </slot>
    </template>

    <template v-slot:item.owner="{ item }">
      <slot
        name="item-owner"
        :item="item"
      >
        <user-avatar-card
          :item="item.owner"
          key-name="full_name"
        />
      </slot>
    </template>

    <template v-slot:item.assigned_to="{ item }">
      <slot
        name="item-assigned_to"
        :item="item"
      >
        <user-avatar-card
          :item="item.assigned_to"
          key-name="full_name"
        />
      </slot>
    </template>

    <template v-slot:item.user="{ item }">
      <slot
        name="item-user"
        :item="item"
      >
        <user-avatar-card
          :item="item.user"
          key-name="full_name"
        />
      </slot>
    </template>
    <template v-slot:item.approver="{ item }">
      <slot
        name="item-approver"
        :item="item"
      >
        <user-avatar-card
          :item="item.approver"
          key-name="full_name"
        />
      </slot>
    </template>

    <template v-slot:item.submitter="{ item }">
      <slot
        name="item-submitter"
        :item="item"
      >
        <user-avatar-card
          :item="item.submitter"
          key-name="full_name"
        />
      </slot>
    </template>

    <template v-slot:item.full_name="{ item }">
      <slot
        name="item-full_name"
        :item="item"
      >
        <user-avatar-card
          :item="item"
          key-name="full_name"
        />
      </slot>
    </template>

    <template v-slot:item.billable="{ item }">
      <slot
        name="item-billable"
        :item="item"
      >
      </slot>
    </template>

    <template v-slot:item.last_submitted_status="{ item }">
      <slot
        name="item-last_submitted_status"
        :item="item"
      >
      </slot>
    </template>
    <template v-slot:item.requester_fullname="{ item }">
      <slot
        name="item-requester_fullname"
        :item="item"
      >
      </slot>
    </template>
    <template v-slot:item.bu_head="{ item }">
      <slot
        name="item-bu_head"
        :item="item"
      >
        <user-avatar-card
          :item="item.bu_head"
          key-name="full_name"
        />
      </slot>
    </template>

    <template v-slot:item.allocation="{ item }">
      <slot
        name="item-allocation"
        :item="item"
      >
      </slot>
    </template>

    <!-- No data -->
    <template v-slot:no-data>
      <div class="empty-state">
        <v-icon large>
          mdi-alert-circle-outline
        </v-icon>
        <h2>{{ no_data_title }}</h2>
        <p>{{ no_data_description }}</p>
      </div>
    </template>
    <template v-slot:item.task="{ item }">
      <slot
        name="item-task"
        :item="item"
      >
      </slot>
    </template>

    <template v-slot:item.resource_cost="{ item }">
      <slot
        name="item-resource_cost"
        :item="item"
      >
      </slot>
    </template>

    <template v-slot:item.invoice_amount="{ item }">
      <slot
        name="item-invoice_amount"
        :item="item"
      >
      </slot>
    </template>

    <template v-slot:item.cost="{ item }">
      <slot
        name="item-cost"
        :item="item"
      ></slot>
    </template>
  </v-data-table>
</template>

<script>

// Components
import TableColoumnConfig from '@/components/DataTable/TableColoumnConfig.vue'
import BaseButton from '@/components/Button/BaseButton.vue'
import UserAvatarCard from '@/components/Users/UserAvatarCard.vue'

// Mixins
import { Helper } from '@/mixins/Helper'
import { bus } from '@/main'

export default {

  components: {
    TableColoumnConfig,
    BaseButton,
    UserAvatarCard,
  },
  mixins: [Helper],

  props: {
    options: {
      // store_action_name
    },

    handlerow: { default: true },
    show_select: { default: true },
    show_select_checkbox: { default: false },
    type: { default: null },
    title: { default: null },
    extra_param: { default: '&' },
    project_relation: { default: 'project_details' },
    no_data_title: { default: 'No Data Available' },
    no_data_description: {
      default:
        "We couldn't find any data for this table. Please check back later or contact support if you believe this is an error.",
    },
    showFilter: { default: true },
  },

  data() {
    return {
      table_pagination: {},
      headers: [],
      headers_list: [],
      items: [],
      selected: [],
      loader: false,
      temp_query: '',
      search_text: '',
      filterEnabled: {
        include_query: {},
        exclude_query: {},
      },
    }
  },

  computed: {
    generate_headers() {
      return this.headers.filter(obj => obj.is_default)
    },
  },

  // mounted() {
  //   //  API to get Field values
  //   this.$store
  //     .dispatch(this.options.store_action_name, 'fields/')
  //     .then(data => {
  //       this.headers_list = data.data
  //       this.field_fetch = false
  //       this.headers = this.headers_list
  //     })
  //     .catch(err => {})
  // },

  watch: {
    table_pagination: {
      handler(value) {
        this.get_list(value)
      },
    },

    selected(values) {
      this.$emit('item-clicked', values)
    },
  },

  created() {
    bus.$on('filter_query_emit', (query, noFilter) => {
      this.filterEnabled = noFilter
      this.get_list({}, query)
      this.$store.dispatch('CloseDrawer')
    })

    bus.$on('remove_filter_query_emit', (query, noFilter) => {
      this.filterEnabled = noFilter
      this.get_list({}, '&')
      this.$store.dispatch('CloseDrawer')
    })
  },

  methods: {
    customRowClass() {
      return 'custom-row-class'
    },

    search() {
      console.log('Search text', this.search_text)
      this.get_list({ view: `&search=${this.search_text}` })
    },

    handleClick(items) {
      if (this.handlerow) {
        this.generate_route(items, this.type)
      }
    },

    set_header(header) {
      const parsed = JSON.stringify(header)
      localStorage.setItem(this.type, parsed)

      this.$store.dispatch('Snackbar', {
        bar: true,
        color: 'success',
        text: 'Config Saved Sucessfully ',
      })
      this.headers = header
    },

    get_list(value, temp_query = null) {
      if (temp_query) {
        this.temp_query = temp_query
      }

      this.loader = true
      let query = ''

      if (this.$route.params.pid) {
        query = this.$route.params.pid
      } else if (this.$route.params.pid) {
        query = this.$route.params.pid
      }
      let query_param = `?${this.project_relation}=${query}&${this.project_relation}=${query}`
      try {
        // Views
        if (value && value.view) {
          query_param += value.view
        }

        // Views
        if (this.temp_query) {
          query_param += this.temp_query
        }

        // Sort By Query Generation
        if (value && value.sortBy && value.sortBy.length >= 1) {
          for (const [i, v] of value.sortBy.entries()) {
            if (value.sortDesc[i]) {
              query_param += `&ordering=-${v}&`
            } else {
              query_param += `&ordering=${v}&`
            }
          }
        } else {
          query_param += '&ordering=-submitted_date&'
        }
      } catch (err) {
        console.error(err)
      }

      // Pagination
      try {
        query_param += `&page=${value.page ? value.page : 1}`
      } catch (_) {}

      //  API Call
      this.$store
        .dispatch(this.options.store_action_name, query_param + this.extra_param)
        .then(data => {
          // this.headers = data.data.columns;
          if (localStorage.getItem(this.type)) {
            const data = JSON.parse(localStorage.getItem(this.type))
            this.headers = data
          } else {
            this.headers = data.data.columns
            const parsed = JSON.stringify(data.data.columns)
            localStorage.setItem(this.type, parsed)
          }

          this.items = data.data
          this.loader = false
          bus.$emit('header_emit', data.data)
        })
        .catch(err => {
          console.error(err)
          this.loader = false
        })
    },

    resourcerequestsuccess(click, response) {
      this.$store.dispatch('Snackbar', {
        bar: true,
        color: status_color(response.status),
        text: `Resource Request #${response.data.id} Updated ...`,
      })
      this.$store.dispatch('CloseDrawer')
    },

    removeFields() {
      localStorage.removeItem(this.type)
    },

    getFilterCount() {
      return Object.keys(this.filterEnabled.include_query).length + Object.keys(this.filterEnabled.exclude_query).length
    },

    generateExtraParams() {
      const include_query = Object.keys(this.filterEnabled.include_query)
      const exclude_query = Object.keys(this.filterEnabled.exclude_query)

      if (include_query.length < 1 && exclude_query.length < 1) {
        return ''
      }
      let params = ''
      if (include_query.length > 0) {
        params += `&include_query=${JSON.stringify(this.filterEnabled.include_query)}`
      }

      if (exclude_query.length > 0) {
        params += `&exclude_query=${JSON.stringify(this.filterEnabled.exclude_query)}`
      }

      return params
    },
  },
}
</script>

<style lang="css" scoped>
.row-pointer >>> tbody tr :hover {
  cursor: pointer;
}
.custom-row-class:hover {
  background-color: rgba(0, 150, 150, 0.2) !important; /* Replace with your desired color */
}
</style>
