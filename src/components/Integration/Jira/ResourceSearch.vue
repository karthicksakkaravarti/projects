<template>
  <div>

    <!-- <Resources ref="resources" :pid="$route.params.pid"> </Resources> -->
  </div>
</template>

<script>
import FormGenerator from '@/components/Forms/FormGenerator.vue'
import Section from '@/components/Helpers/Section.vue'
import ViewList from '@/components/DataTable/ViewList.vue'
import Team from '@/components/AutoComplete/Team.vue'
// import Resources from '@/apps/project/components/Resources.vue'
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
    // Resources,
    BaseButton
  },
  mixins: [Setup, Project],

  data() {
    return {
      form: [{}],
      field: {
        value: null,
      },
      search_method: true,
      selected_resource: [],
    }
  },
  mounted() {
    this.get_form()
    this.call_resource_search()
  },
  created() {
    bus.$on('add_resource_to_team', (value, options, value2) => {
      console.log(options.ResourceConfirmation_Props)
      // this.add_resource_to_team()
      this.PROJECT_API_PROJECT_POST({
        custom_action: this.$route.params.pid + '/add_resource',
        data: options.ResourceConfirmation_Props,
        not_execute_extract: true,
      }).then(data => {
        this.$store.dispatch('Snackbar', {
          bar: true,
          color: 'success',
          text: data.data,
        })
        this.$refs.resources.get_resources()
      })
    })
  },
  destroyed() {
    bus.$off('add_resource_to_team')
  },
  methods: {
    add_to_team(resource, item) {
      if (this.field.value) {
        resource['role'] = item.role
        resource['emp_id'] = item.emp_id
        resource['team_name'] = this.$refs.team.search
        resource['team'] = this.field.value
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
              ResourceConfirmation_Props: [resource],
            },
          },
        })
      }
      // If Team Not selected
      else {
        this.$store.dispatch('Snackbar', {
          bar: true,
          color: 'error',
          text: 'Please select Team',
        })
      }
    },
    get_form() {
      this.loading = true
      this.SETUP_API_FORMMODEL_GET('get_form/?form_name=' + 'ResourceSearch' + '&pid=' + this.$route.params.pid).then(
        data => {
          this.form = data.data
          // this.loading = false
        },
      )
    },
    item_clicked(item) {
      this.selected_resource = item
    },
    call_resource_search(value) {
      if (this.$refs.form && this.$refs.form.form_validation()) {
        var query_params = '?search_type=available'

        for (var query of this.$refs.form.Form) {
          if (query.value) {
            query_params += '&' + query.dbfield + '=' + query.value
          }
        }
        console.log('query_params', query_params)
        this.$refs.search_result.get_list({ view: query_params }, query_params)
      } else {
        console.log('Else block')
      }
    },
  },
}
</script>

<style>
</style>
