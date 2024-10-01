  <template>
  <div>
    <v-checkbox
      color="primary"
      :error-messages="error_message"
      :autofocus="autofocus"
      :type="type"
      :label="label"
      :rules="rules"
          hide-details="auto"

      :disabled="disabled"
      :readonly="readonly"
      :prepend-icon="prependicon"
      :append-icon="appendicon"
      :prepend-inner-icon="prependinnericon"
      :append-outer-icon="appendoutericon"
      v-model="field.value"
      dense
    ></v-checkbox>
  </div>
</template>

<script>
import { Rules } from '@/mixins/Rules'

export default {
  mixins: [Rules],
  props: {
    label: { required: true, type: String },
    field: { default: {} },
    prependicon: { default: '' },
    appendicon: { default: '' },
    error_message: { default: null },
    prependinnericon: { default: '' },
    appendoutericon: { default: '' },
    disabled: { default: false },
    readonly: { default: false },
    type: { default: 'String' },
    value: { default: '' },
    autofocus: { default: false },
  },

  methods: {},
}
</script>





<style>
</style>