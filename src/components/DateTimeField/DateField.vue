<template>
  <v-menu
    v-model="field.menu"
    :disabled="readonly"
    :close-on-content-click="false"
    :nudge-right="40"
    transition="scale-transition"
    offset-y
    min-width="150"
    :readonly="readonly"
    :prepend-inner-icon="prependinnericon"
  >
    <template v-slot:activator="{ on }">
      <v-text-field
          hide-details="auto"
          :error-messages="error_message"
        color="primary"
        :append-icon="appendicon"
            :outlined="outlined"
        v-model="field.value"
        :rules="rules"
        dense
        :clearable="!readonly"
        :label="label"
        :prepend-inner-icon="prependinnericon"
        :prependinnericon="prependicon"
        readonly
        v-on="on"
        required
      >
        <template v-slot:label> {{ label }} <span style="color: red" v-if="field && field.required">*</span> </template>
      </v-text-field>
    </template>
    <v-date-picker color="primary" v-model="field.value" :min="mindate" :max="maxdate" @input="field.menu = false">
    </v-date-picker>
  </v-menu>
</template>

<script>
import { Rules } from '@/mixins/Rules'

export default {
  mixins: [Rules],
  props: {
    label: { required: true, type: String },
    field: { default: {} },
    prependicon: { default: '' },
    error_message: { default: null },
    readonly: { default: false },
    appendicon: { default: '' },
    prependinnericon: { default: '' },
    appendoutericon: { default: '' },
    maxdate: { default: '' },
    mindate: { default: '' },
    outlined: { default: false },
  },
}
</script>

<style lang="scss">
.v-picker {
  .v-picker__body {
    width: 250px !important;
  }
}
.v-date-picker-title__date {
  font-size: 10px !important;
}
</style>