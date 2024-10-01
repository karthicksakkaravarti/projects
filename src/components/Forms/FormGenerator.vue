<template>
  <div>
    <div class="ma-4">
      <v-alert border="left" dense icon="mdi-alert-circle" class="mb-5"
          v-if="error_message" color="error" title="Error" dark prominent >
          {{ error_message }}
      </v-alert>
      <v-form :disabled="disabled" ref="Form_Ref" v-model="form">
        <v-row>
          <template v-for="(field, key) in formData">
            <v-col cols="12" v-if="condition_field(field)" :sm="field.sm" v-bind:key="key">
              <components :label="field.name" :rules="field.rules" :readonly="field.readonly" :outlined="field.outlined"
                :disabled="field.disabled" :clearable="field.clearable" :rows="field.rows" :is="field.fieldtype"
                :error_message="field.error_message" :hint="field.hint" :multiple="field.multiple"
                :maxdate="field.maxdate_field
                  ? formData.filter(obj => {
                    return obj.dbfield == field.maxdate_field && obj.fieldtype == 'DateField'
                  })[0].value
                  : field.maxdate
                  " 
                :mindate="field.mindate_field
                  ? formData.filter(obj => {
                    return obj.dbfield == field.mindate_field && obj.fieldtype == 'DateField'
                  })[0].value
                  : field.mindate
                  " :field="field" 
                :itemtext="field.itemtext" :itemvalue="field.itemvalue" :dropdownitems="field.valuelist"
                :type="field.type" :prependicon="field.prependicon" :prependinnericon="field.prependinnericon"
                :prefix="field.prefix" :appendicon="field.appendicon">
              </components>
            </v-col>
          </template>
        </v-row>
        <!-- <v-row v-if="$store.state[drawer].DrawerForm.length >= 1">
          <Button
            :disabled="disabled"
            title="Submit"
            click=""
            @success="success"
            :options="{
              refs: $refs,
              validate_form: true,
              validate_form_name: 'Form_Ref',
              custom_action: 'cr_create',
              data: $store.state[drawer].DrawerForm,
            }"
          />
          <Button :disabled="disabled" color="error" title="Cancel" click="CloseDrawer" :options="{}" />
        </v-row> -->
      </v-form>
    </div>
  </div>
</template>

<script>
// Common Imports in the mixin
import { ModuleImport } from '@/mixins/ModuleImport'

import { status_color, exception_rest_api_handler } from '@/helper'
import { bus } from '@/main'

export default {
  mixins: [ModuleImport],
  props: {
    disabled: { default: false },
    drawer: { default: 'Drawer' },
    Form: { default: null },
  },
  data: () => ({
    form: false,
    error_message: ''
  }),
  computed: {
    drawerModel () {
      return this.$store.state[this.drawer].DrawerModel;
    },
    formData() {
      if (this.Form) {
        return this.Form
      } else {
        return this.$store.state[this.drawer].DrawerForm
      }
    },
  },
  watch: {
    drawerModel () {
      this.error_message = '';
    }
  },
  methods: {
    condition_field(field) {
      if (field.fieldtype == 'Hiden') {
        return false
      }
      if (field.conditionfield && field.conditionfield1) {
        return (
          this.$store.state[this.drawer].DrawerForm.filter(obj => {
            return obj.dbfield == field.conditionfield && String(obj.value) == String(field.conditionvalue)
          }).length == 1 &&
          this.$store.state[this.drawer].DrawerForm.filter(obj => {
            return obj.dbfield == field.conditionfield1 && String(obj.value) == String(field.conditionvalue1)
          }).length == 1
        )
      } else if (field.conditionfield) {
        return (
          this.$store.state[this.drawer].DrawerForm.filter(obj => {
            return obj.dbfield == field.conditionfield && String(obj.value) == String(field.conditionvalue)
          }).length == 1
        )
      } else {
        return true
      }
    },
    // Form validation
    form_validation() {
      if (this.$refs['Form_Ref'].validate()) {
        try {
          this.$store.dispatch('EnableDrawerLoader')
          this.$store
            .dispatch(this.$store.state[this.drawer].DrawerFormSubmit['store_action_name'], {
              custom_action: this.$store.state[this.drawer].DrawerFormSubmit['custom_action'],
              data: this.$store.state[this.drawer].DrawerForm,
            })
            .then(data => {
              // this.$emit('success', this.click, data)
              if (this.$store.state[this.drawer].DrawerFormType == 'NewCustomer') {
                bus.$emit('customer_form_success', data, this.$store.state[this.drawer].DrawerFormType)
              } else {
                bus.$emit(
                  'form_success',
                  data,
                  this.$store.state[this.drawer].DrawerFormType,
                  this.$store.state[this.drawer].DrawerActionType,
                )
              }
              // this.$store.dispatch('CloseDrawer')
              this.$store.dispatch('DisableDrawerLoader')
            })
            .catch(err => {
            //   this.$emit('error', this.click, err.response.data)
              this.handleError(this.click, err.response.data)
              this.$store.dispatch('DisableDrawerLoader')
            })
        } catch (_) {
          this.$store.dispatch('DisableDrawerLoader')

          return true
        }
        this.$store.dispatch('DisableDrawerLoader')

        return true
      } else {
        this.$store.dispatch('DisableDrawerLoader')

        return false
      }
    },
    success(click, api_response) {
      this.$store.dispatch('Snackbar', {
        bar: true,
        color: status_color(api_response.status),
        text: 'CR #' + api_response.data.id + ' Created ...',
      })
      this.$store.dispatch('CloseDrawer')
      // Refresh Project Table
      bus.$emit('refresh_project_table')
      console.log('Calling in FormGeneration')
    },

    handleError (click, response) {
      const data = exception_rest_api_handler(response);
      this.error_message = data;
    }

  },
}
</script>

<style></style>
