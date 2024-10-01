<template>
  <v-autocomplete
    color="primary"
    v-model="field.value"
    :item-text="itemtext"
    :item-value="itemvalue"
    :rules="rules"
    hide-details="auto"
    dense
    :items="dropdownitems"
    :placehoder="placehoder"
    :label="label"
    :outlined="outlined"
    :clearable="clearable"
    :multiple="multiple"
    :readonly="readonly"
    @change="fireEvent('change')"
    @input="fireEvent('input')"
  >
    <template v-if="!readonly" v-slot:label> {{ label }} <span style="color: red" v-if="field && field.required">*</span> </template>
  </v-autocomplete>
</template>

<script>
import BaseButton from '@/components/Button/BaseButton.vue'
export default {
    components: {
        BaseButton,
    },
    
    props: {
        label: { required: true, type: String },
        field: { default: {} },
        rows: { default: 5 },
        rowheight: { default: 20 },
        prependicon: { default: '' },
        appendicon: { default: '' },
        prependinnericon: { default: '' },
        appendoutericon: { default: '' },
        dropdownitems: [],
        placehoder: { default: '' },
        itemtext: '',
        itemvalue: '',
        outlined: { default: false },
        clearable: { default: false },
        multiple: {default : false},
        readonly: {default : false},
    },

    computed: {
        rules() {
            var data = []
            if (this.field && this.field.required) {
                data.push(v => v === 0 || !!v || this.field.name + ' is required')
            } else {
                data = []
            }
            return data
        },
    },

    watch: {},

    methods: {
        fireEvent(action) {
            this.$emit(action)
        }
    },
}
</script>

<style>
</style>