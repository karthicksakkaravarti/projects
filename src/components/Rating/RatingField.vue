<template>
    <div>
        <div class="text-center">
            <span class="font-weight-bold">
                {{ label }}
            </span>
        </div>

      <v-rating
        class="text-center"
        hide-details="auto"
        :rules="rules"
        :readonly="readonly"
        v-model="field.value"
        dense
        :length="outOf"
        :size="size"
      >
        <template v-slot:item="props">
            <v-icon color="primary" @click="props.click">
                {{ getIcon(props) }}
            </v-icon>
        </template>
      </v-rating>
    </div>
  </template>

<script>
import { Rules } from '@/mixins/Rules'

export default {
    mixins: [Rules],

    props: {
        label: { required: true, type: String },
        field: { default () { return { value: '' }; } },
        readonly: { default: false },
        outOf: { default: '5' },
        size: { default: '30' },
        value: { default: '0' },
        emptyIcons: { default () { return []; } },
        fullIcons: { default () { return []; } },
    },

    data () {
        return {
            zeorIcons: [
                'mdi-emoticon-cry-outline',
                'mdi-emoticon-sad-outline',
                'mdi-emoticon-neutral-outline',
                'mdi-emoticon-happy-outline',
                'mdi-emoticon-outline'
            ],
            fillIcons: [
                'mdi-emoticon-cry',
                'mdi-emoticon-sad',
                'mdi-emoticon-neutral',
                'mdi-emoticon-happy',
                'mdi-emoticon'
            ]
        };
    },

    methods: {
        getIcon (props) {
            const FillIcons = this.fullIcons.length > 0 ? [...this.fullIcons] : [...this.fillIcons];
            const EmptyIcons = this.emptyIcons.length > 0 ? [...this.emptyIcons] : [...this.zeorIcons];
            return props.isFilled ? FillIcons[props.value - 1] : EmptyIcons[props.index]
        },
    }
}
</script>

<style>
</style>