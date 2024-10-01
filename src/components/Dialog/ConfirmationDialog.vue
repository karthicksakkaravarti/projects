<template>
  <div>
    <div>
      <v-dialog v-model="$store.state.ConfirmationDialog.Dialog" max-width="500" persistent>
        <v-card :disabled="$store.state.ConfirmationDialog.Loader">
          <v-card-title class="text-h5 mb-2">{{ $store.state.ConfirmationDialog.Title ? $store.state.ConfirmationDialog.Title: 'Confirmation'  }}</v-card-title>
          <v-card-text>
            <v-alert border="left" dense icon="mdi-alert-circle" class="mb-5"
                v-if="error_message" color="error" title="Error" dark prominent >
                {{ error_message }}
            </v-alert>
            {{ $store.state.ConfirmationDialog.Body }}
             <components v-if="$store.state.ConfirmationDialog.SubmitButton.options && $store.state.ConfirmationDialog.SubmitButton.options.is_component"
              :is="$store.state.ConfirmationDialog.SubmitButton.options.is_component"
             :props="$store.state.ConfirmationDialog.SubmitButton.options.ResourceConfirmation_Props"
              ></components>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <template>
              <Button :text="true" color="default" title="Close" click="CloseConfirmationDialog" :options="{}" />
              <Button
                @success="success" @error="handleError"
                :text="$store.state.ConfirmationDialog.SubmitButton.text"
                :color="$store.state.ConfirmationDialog.SubmitButton.color"
                :title="$store.state.ConfirmationDialog.SubmitButton.title"
                :click="$store.state.ConfirmationDialog.SubmitButton.click"
                :options="$store.state.ConfirmationDialog.SubmitButton.options"
                :loading="$store.state.ConfirmationDialog.Loader"
              />&nbsp;&nbsp;&nbsp;
            </template>
          </v-card-actions>
        </v-card>
      </v-dialog>
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
  },
  data: () => ({
    form: false,
    error_message: ''
  }),
  computed: {
    dialog () {
      return this.$store.state.ConfirmationDialog.Dialog;
    }
  },
  watch: {
    dialog () {
      this.error_message = '';
    }
  },
  methods: {
    success(click, options, api_response) {
      this.$store.dispatch('CloseConfirmationDialog')
      console.log('-->', click)
      console.log('-->', options)
      if (options && options.on_success && options.on_success.bus_emit) {
        bus.$emit(options.on_success.bus_emit, api_response, options)
      } else if (options && options.on_success && options.on_success.route) {
        this.$router.push(options.on_success.route)
      } else {
        bus.$emit('form_success', api_response, '')
      }

      if (api_response && api_response.data && api_response.data.App === 'SubmitBuHead') {
        this.$store.dispatch('Snackbar', {
          bar: true,
          color: 'success',
          text: api_response.data.message,
        })
        this.$store.dispatch('CloseDrawer', {})
        localStorage.removeItem('newProjectID')
        if (this.$route.name === 'Project') {
          this.$router.go();
        } else {
          this.$router.push({name: 'Project'})
        }
      }
      // this.$router.push({ name: 'Project' })

      // bus.$emit('form_success', data, this.$store.state['ConfirmationDialog'].DrawerFormType, this.$store.state[''].DrawerActionType)
    },
    handleError (click, response) {
      const data = exception_rest_api_handler(response);
      this.error_message = data;
    }
  },
}
</script>

<style>
</style>
