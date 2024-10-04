<template>
  <v-autocomplete
  filled
  rounded
  small
    hide-details
    dense
    color="primary"
    style="max-width: 200px"
    v-model="model"
    @change="view_changed"
    :item-text="item_text"
    :item-value="item_value"
    :items="items"
  ></v-autocomplete>
</template>

<script>
import { bus } from '@/main'

export default {
  computed: {
    filteredItems() {
      return this.items.filter(item => {
        return item.name.toLowerCase().match(this.search)
      })
    },
  },
  created() {
    bus.$on('header_emit', response => {
      this.items = response[this.lookup + '_list']
      this.response =  response
      if (this.lookup_by) {
        this.model = response[this.lookup][this.lookup_by]
      } else {
        this.model = response[this.lookup]
      }
    })
  },
  props: {
    lookup: { default: 'customview' },
    item_text: { default: null },
    item_value: { default: null },
    lookup_by: { default: null },
    label: { default: 'Views' },
    type: { default: null },
  },
  data() {
    return {
      search: '',
      items: [],
      model: '',
      response: []
    }
  },
  methods: {
    view_changed() {
      this.$emit('refresh_table', { view: "&"+this.lookup+"="+this.model, type: this.type })

    },
  },
}
</script>

