<template>
    <div>
        <div>
            <div v-if="FORMDATA">
                <!-- {{ FORMDATA[0]['fields'] }} -->
                <v-row class="col-12 ma-0 pa-0">
                    <div class="d-flex flex justify-space-between ma-1">
                        <v-spacer></v-spacer>
                        <v-chip @click="removeFilter" small>
                            <v-icon small>mdi-close-circle-outline</v-icon>&nbsp;CLEAR
                        </v-chip>
                    </div>
                </v-row>
                <div v-for="field in FORMDATA[0]['fields']" :key="field.name">
                    <v-row class="col-12 ma-0 pa-0">
                        <v-col cols="12" class="pb-0 pt-0" style="cursor: pointer;">
                            <v-checkbox class="ma-0 pa-0" v-model="field.show" :label="field.name"></v-checkbox>
                        </v-col>
                    </v-row>
                    <v-row class="col-12 ma-0 pa-0" v-if="field.show">
                        <v-col cols="4">
                            <v-select v-model="field.filter_type" dense label="Condition"
                                outlined item-text="key" item-value="value"
                                :items="field.field_search_list" hide-details="auto" no-padding>
                            </v-select>
                        </v-col>
                        <v-col cols="8">
                            <components :rules="field.rules" :outlined="true" label="Serach Text"
                                :is="field.field_type" :field="field" :itemtext="field.itemtext" :itemvalue="field.itemvalue" :dropdownitems="field.dropdown_values" :prependicon="field.prependicon"
                                :prependinnericon="field.prependinnericon" :prefix="field.prefix" :appendicon="field.appendicon" :multiple=true>
                            </components>
                        </v-col>
                    </v-row>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { ModuleImport } from '@/mixins/ModuleImport'
import { status_color } from '@/helper'
import { bus } from '@/main'
export default {

    mixins: [ModuleImport],
    
    data() {
        return {
            showBar: false,
            defaultApp: 'Project',
            panel : [],
        }
    },

    methods: {
        filter_generation(){
            var selected_filter = this.FORMDATA[0]['fields'].filter(obj => { return obj.show })
            if (selected_filter && selected_filter.length == 0){
                this.$store.dispatch('Snackbar', {
                    bar: true, color: status_color(400),
                    text: 'Select Atleast 1 field to filter',
                })
            } else {
                var include_query = {}
                var exclude_query = {}
                let generated_query = ``
                for (var query of selected_filter){
                    if (query.filter_type.startsWith("not")){
                        exclude_query[query.dbfield+query.filter_type.substr(3-query.filter_type.length)] = query.value 
                    }else {
                        include_query[query.dbfield+query.filter_type] = query.value
                    }
                }

                const totalFilterEnabled = {
                    include_query: include_query,
                    exclude_query: exclude_query
                };

                if (Object.keys(include_query).length > 0) {
                    generated_query = generated_query + `&include_query=${JSON.stringify(include_query)}`
                }

                if (Object.keys(exclude_query).length > 0) {
                    generated_query = generated_query + `&exclude_query=${JSON.stringify(exclude_query)}`
                }

                bus.$emit('filter_query_emit', generated_query, totalFilterEnabled)
                // this.$store.dispatch('EnableDrawerLoader')
                // this.$store.dispatch(this.$store.state[this.drawer].DrawerFormSubmit['store_action_name'], query=query)
                // .then(data => {
                //     this.$store.dispatch('DisableDrawerLoader')
                //     console.log(data)
                // }).catch(err => {
                //     console.log(err)
                //     this.$store.dispatch('DisableDrawerLoader')
                // })
            }
        },

        removeFilter() {
            const totalFilterEnabled = {
                include_query: {},
                exclude_query: {}
            }
            bus.$emit('remove_filter_query_emit', '', totalFilterEnabled)
        }
    },

    props: {
        FORMDATA : {default : false },
        drawer: { default: 'Drawer' },
    }
}

</script>
<style scoped>
/* Remove padding and margin on the v-select */
.v-select {
  padding: 0 !important;
  margin: 0 !important;
}
</style>