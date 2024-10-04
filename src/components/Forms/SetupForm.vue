<template>
  <v-row class="ma-1">
    <v-col cols="6">
      <v-card elevation="0" :disabled="loading" :loading="loading">
         <v-card-title
          ><i>{{ form }}</i> - Form Edit</v-card-title
        >
        <v-card-text>
          <v-sheet id="scrolling-techniques-7" class="overflow-y-auto" max-height="600">
            <v-container style="height: 1500px">
              <codemirror v-model="EditForm" :options="cmOption" />
            </v-container>
          </v-sheet>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn class="mt-5" color="primary" @click="save_form" small>Save Form</v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
    <v-col cols="6">
      <v-card elevation="0" :disabled="loading" :loading="loading">
        <v-card-title
          ><i>{{ form }}</i> - Form Preview</v-card-title
        >
        <v-card-text>
          <v-sheet id="scrolling-techniques-7" class="overflow-y-auto" max-height="600">
            <v-container style="height: 1500px">
              <FormGenerator :Form="Form"></FormGenerator>
            </v-container>
          </v-sheet>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import { Setup } from '@/mixins/Setup'
import { CodeMirror } from '@/mixins/CodeMirror'
import { status_color } from '@/helper'

import FormGenerator from '@/components/Forms/FormGenerator.vue'
// import codemirror from '@/components/Codemirror/codemirror.vue'

export default {
  mixins: [Setup, CodeMirror],
  components: {
    FormGenerator,
  },
  props: {
    form: {},
  },
  data() {
    return {
      Form: null,
      EditForm: null,
      loading: false,
    }
  },
  watch: {
    EditForm(value) {
      this.Form = JSON.parse(value)
    },
    form(value) {
      this.get_form()
    },
  },
  mounted() {
    this.get_form()
  },
  methods: {
    replacer(i, val) {
      if (val !== null) {
        return val // change null to empty string
      }
      // else {
      //   return val // return unchanged
      // }
    },
    get_form() {
      this.loading = true
      this.SETUP_API_FORMMODEL_GET('get_form/?form_name=' + this.form).then(data => {
        this.EditForm = JSON.stringify(data.data, null, 2)
        this.loading = false
      })
    },
    save_form() {
      this.loading = true

      var payload = JSON.parse(this.EditForm)
      console.log(payload)
      Object.keys(payload).forEach(key => {
        if (payload[key] === null && key != 'valuelist') {
          delete payload[key]
        }
      })
      for (var i of payload){
        i['valuelist'] = []
      }
      
      this.SETUP_API_FORMMODEL_POST({
        query_param: this.$route.params.id,
        data: {
          layout: JSON.stringify(
            {
              data: payload,
            },
            this.replacer,
            2,
          ),
        },
      })
        .then(response => {
          this.loading = false
          this.$store.dispatch('Snackbar', {
          bar: true,
          color: status_color(response.status),
          text: response.data.name +" Form Updated ...",
        })
        })
        .catch(() => {
          this.loading = false
        })
      console.log(this.$route.params.id)
    },
  },
}
</script>

<style>
.CodeMirror {
  /* Set height, width, borders, and global font properties here */
  font-family: monospace;
  height: 100%;
}
</style>