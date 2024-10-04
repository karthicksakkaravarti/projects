<template>
  <v-container>
    <v-row>
      <v-col>
        <v-select v-show="!showTotalOnly" prepend-icon="mdi-clock-time-four-outline" :rules="rules" v-model="from" :items="times"
          hide-details="auto" label="From"></v-select>
      </v-col>

      <v-col>
        <v-select v-show="!showTotalOnly" v-model="to" :items="times" prepend-icon="mdi-clock-time-four-outline" label="To" :rules="rules"
          hide-details="auto"></v-select>
      </v-col>

      <v-col class="ma-0 pa-0">
        <v-text-field :rules="rules" v-model="worked" label="Worked Hours" @input="calculateTo">
          <template v-if="!readonly" v-slot:label>  Worked Hours <span style="color: red" v-if="field && field.required">*</span> </template>
        </v-text-field>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { Rules } from '@/mixins/Rules'

export default {
  mixins: [Rules],

  props: {
    label: { required: true, type: String },
    field: { default: {} },
    prependicon: { default: '' },
    readonly: { default: false },
    appendicon: { default: '' },
    prependinnericon: { default: '' },
    appendoutericon: { default: '' },
    maxdate: { default: '' },
    mindate: { default: '' },
    outlined: { default: false },
    showTotalOnly: { default: false }
  },

  data() {
    return {
      from: '',
      to: '',
      worked: '',
      times: this.generateTimes(),
    }
  },
  methods: {
    generateTimes() {
      const times = [];
      for (let i = 0; i < 24; i++) {
        for (let j = 0; j < 60; j += 30) {
          const hour = i < 10 ? '0' + i : i;
          const minute = j < 10 ? '0' + j : j;
          times.push(`${hour}:${minute}`);
        }
      }
      return times;
    },
    parseHours(duration) {
      // Extract the numeric part of the string
      var hours = parseFloat(duration);

      // Return the parsed hours value
      return hours;
    },
    calculateWorked() {
      if (this.from && this.to) {
        const fromDate = new Date(`1970-01-01T${this.from}:00Z`);
        const toDate = new Date(`1970-01-01T${this.to}:00Z`);
        let diff = toDate - fromDate;
        if (diff < 0) diff += 24 * 60 * 60 * 1000; // if time crosses midnight
        const hours = Math.floor(diff / 36e5);
        if (hours) {
          this.worked = `${hours}h`;
        }

        this.field.value = {
          start_time: this.from,
          end_time: this.to,
          duration: this.parseHours(this.worked)+':00:00',
        }
      }
    },
    calculateTo() {
      if (this.from && this.worked) {
        const workedHours = parseInt(this.worked.replace('h', ''));
        const fromDate = new Date(`1970-01-01T${this.from}:00Z`);
        fromDate.setHours(fromDate.getHours() + workedHours);
        const hour = fromDate.getUTCHours() < 10 ? '0' + fromDate.getUTCHours() : fromDate.getUTCHours();
        const minute = fromDate.getUTCMinutes() < 30 ? '00' : '30';
        this.to = `${hour}:${minute}`;
      }
    },
  },
  watch: {
    from() {
      this.calculateWorked();
    },
    to() {
      this.calculateWorked();
    },
  },
  created() {
    const date = new Date();
    const hour = date.getHours() < 10 ? '0' + date.getHours() : date.getHours();
    const minute = date.getMinutes() < 30 ? '00' : '30';
    // this.from = `${hour}:${minute}`;
    this.from = `10:00`;
    this.to = this.from;
  },
};
</script>
