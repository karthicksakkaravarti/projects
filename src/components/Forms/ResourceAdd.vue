<template>
  <div>
    <div>
      <FormGenerator
        ref="form"
        :form="form"
      >
      </FormGenerator>
    </div>
    <div class="d-flex flex-row-reverse ma-2">
      <v-btn
        color="primary"
        small
        @click="call_resource_search"
      >
        Search
      </v-btn>

      <div class="mr-2">
        <Team
          ref="team"
          :field="field"
          label="Team"
          itemtext="team_name"
          itemvalue="id"
        ></Team>
      </div>
      <div>
        <v-btn
          color="primary"
          text
          class="mr-2"
          dense
          small
          @click="
            $store.dispatch('OpenDialogOnClick', {
              Dialog: true,
              Title: 'Add New Team',
              RefName: 'NewTeam_Ref',
              API_FORM: true,
              DialogEditType: 'new',
              FormName: 'NewTeam',
              DialogMutation: 'mutation__dialog',
              DialogExtraParam: `&project_details=${$route.params.pid}`,
              SubmitButton: { title: 'Add', text: true, color: 'success', click: 'TeamResourceStore/TeamNameCreate' },
            })
          "
        >
          Add New Team
        </v-btn>
      </div>
    </div>
    <div class="ma-3">
      <div class="d-flex justify-space-between">
        <Section label="Available Resources"></Section><br />
        <div>
          <!-- <h3>
                    <b> Resource Selected</b>
                </h3> -->
          <v-btn
            v-if="selected_resource.length >= 1"
            color="primary"
            outlined
            x-small
            @click="add_multiple_resource_to_team(selected_resource)"
          >
            Add ({{ selected_resource.length }}) resource
          </v-btn>
        </div>
      </div>
      <br />
      <ViewList
        ref="search_result"
        type="resource_search"
        :handlerow="false"
        :options="{
          store_action_name: 'ProjectStore/PROJECT_API_RESOURCE_SEARCH',
        }"
        @item-clicked="item_clicked"
      >
        <template #item-title="{ item }">
          {{ item.title }}
        </template>
        <template #item-availability="{ item }">
          <div style="max-width: 100px ma-1">
            <v-timeline
              class="ma-2"
              dense
            >
              <v-timeline-item
                v-for="avl in item.availability"
                :key="avl"
                color="green"
                small
              >
                <v-row justify="space-between">
                  <v-col cols="7">
                    <v-chip
                      class="white--text ml-0"
                      color="green"
                      label
                      small
                    >
                      Available
                    </v-chip> From:
                    <b>{{ avl.start_date }}</b> To: <b>{{ avl.end_date }}</b>
                    <!-- <template v-if="avl.start_date != item.a_sd">
                                        <br />
                                        Note: Resource not available from project start date
                                        </template> -->
                    <!-- <template v-if="avl.end_date != item.a_ed">
                                            <br>
                                            Note: Resource not available till project end date
                                            </template> -->
                  </v-col>
                  <v-col
                    class="text-right"
                    cols="5"
                  >
                    {{ avl.available_allocation }} %
                    <v-btn
                      color="primary"
                      text
                      small
                      @click="add_to_team(item, avl)"
                    >
                      + Team
                    </v-btn>
                  </v-col>
                </v-row>
              </v-timeline-item>
            </v-timeline>
          </div>
        </template>
      </ViewList>
    </div>
  </div>
</template>

<script>
import FormGenerator from '@/components/Forms/FormGenerator.vue'
import Section from '@/components/Helpers/Section.vue'
import ViewList from '@/components/DataTable/ViewList.vue'
import Team from '@/components/AutoComplete/Team.vue'
import Resources from '@/apps/project/components/Resources.vue'
import BaseButton from '@/components/Button/BaseButton.vue'
import { Setup } from '@/mixins/Setup'
import { bus } from '@/main'
import { Project } from '@/mixins/Project'

export default {
  components: {
    FormGenerator,
    Section,
    ViewList,
    Team,
    Resources,
    BaseButton,
  },

  mixins: [Setup, Project],

  props: {
    searchTeam: {
      type: Object,
      default() {
        return {
          value: null,
        }
      },
    },
  },

  data() {
    return {
      form: [{}],
      field: this.searchTeam,
      search_method: true,
      selected_resource: [],
    }
  },

  mounted() {
    this.get_form()

    // this.call_resource_search();
  },

  destroyed() {
    bus.$off('add_resource_to_team')
  },

  methods: {
    add_multiple_resource_to_team(resources) {
      const avl = []
      for (const resoure of resources) {
        const temp = resoure.availability[0]
        temp.role = resoure.role
        temp.emp_id = resoure.emp_id
        temp.team_name = this.$refs.team.search
        temp.team = this.field.value
        avl.push(temp)
      }
      if (this.field.value) {
        this.$store.dispatch('OpenConfirmationDialogOnClick', {
          Dialog: true,
          Title: `Adding Resource To Team - ${this.$refs.team.search}`,
          SubmitButton: {
            title: 'Add To Team',
            text: true,
            color: 'success',
            click: 'CloseConfirmationDialog',
            options: {
              on_success: {
                bus_emit: 'add_resource_to_team',
              },
              is_component: 'ResourceConfirmation',
              ResourceConfirmation_Props: avl,
            },
          },
        })
      }

      // If Team Not selected
      else {
        this.$store.dispatch('Snackbar', {
          bar: true,
          color: 'red',
          text: 'Please select Team',
        })
      }
    },

    add_to_team(item, avl) {
      if (this.field.value) {
        avl.role = item.title
        avl.resource_name = item.full_name
        avl.member_id = null
        avl.resource_id = item.username
        avl.allocation = avl.available_allocation
        avl.cost = avl.cost
        avl.emp_id = item.username
        avl.team_name = this.$refs.team.search
        avl.team = this.field.value
        avl.project_details = this.$route.params.pid
        this.$store.dispatch('OpenConfirmationDialogOnClick', {
          Dialog: true,
          Title: `Adding Resource To Team - ${this.$refs.team.search}`,
          SubmitButton: {
            title: 'Add To Team',
            text: true,
            color: 'success',
            click: 'CloseConfirmationDialog',
            options: {
              on_success: {
                bus_emit: 'add_resource_to_team',
              },
              is_component: 'ResourceConfirmation',
              ResourceConfirmation_Props: [avl],
            },
          },
        })
      } else {
        this.$store.dispatch('Snackbar', {
          bar: true,
          color: 'error',
          text: 'Please select Team',
        })
      }
    },

    get_form() {
      const extraParams = this.$store.state.Drawer.DrawerFormSubmit.data
        ? this.$store.state.Drawer.DrawerFormSubmit.data
        : ''
      this.loading = true
      this.SETUP_API_FORMMODEL_GET(
        `get_form/?form_name=ResourceSearch&pid=${this.$route.params.pid}${extraParams || ''}`,
      ).then(data => {
        this.form = data.data
        this.call_resource_search()

        // this.loading = false
      })
    },

    item_clicked(item) {
      this.selected_resource = item
    },

    call_resource_search(value) {
      if (this.$refs.form.form_validation()) {
        let query_params = '&search_type=available'

        for (const query of this.form) {
          if (query.dbfield === 'title') {
            if (query.value) {
              query_params += `&${query.dbfield}=${query.value}`
            } else {
              const extraParams = this.$store.state.Drawer.DrawerFormSubmit.data
                ? this.$store.state.Drawer.DrawerFormSubmit.data
                : ''
              query_params += extraParams
            }
          } else if (query.value) {
            query_params += `&${query.dbfield}=${query.value}`
          }
        }

        if (this.field.value) {
          query_params += `&team=${this.field.value}`
        }

        this.$refs.search_result.get_list({ view: query_params }, query_params)
      } else {
        console.log('Else block')
        this.$store.dispatch('Snackbar', {
          bar: true,
          color: 'error',
          text: 'Please fix the form error.',
        })
      }
    },
  },
}
</script>

<style></style>
