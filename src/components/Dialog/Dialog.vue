<template>
    <div>
        <div v-if="$store.state.Dialog.Dialog">
            <v-dialog v-model="$store.state.Dialog.Dialog" :max-width="$store.state.Dialog.DialogSize" persistent>
                <v-card v-if="$store.state.Dialog.API_FORM">
                    <v-overlay absolute :value="$store.state.Dialog.Loader">
                        <v-progress-circular :size="30" :width="5" color="primary" indeterminate></v-progress-circular>

                    </v-overlay>
                    <v-card-title class="d-flex justify-space-between">
                        <h5 class="text-h5">{{ $store.state.Dialog.Title }}</h5>
                        
                        <div v-if="$store.state.Dialog.FormName === 'LogTime'">
                            <v-btn small :text="true" color="primary" @click="openNewLogForm">Log Multiple</v-btn>
                        </div>
                    </v-card-title>
                    <v-window v-model="$store.state.Dialog.DialogWindow">
                        <v-window-item :value="1">
                            <v-card-text>
                                <v-alert border="left" dense icon="mdi-alert-circle" class="mb-5"
                                    v-if="error_message" color="error" title="Error" dark prominent >
                                    {{ error_message }}
                                </v-alert>
                                <v-form :ref="$store.state.Dialog.RefName" v-model="form" class="mt-2">
                                    <v-row>
                                        <template v-for="(field, key) in $store.state.Dialog.DialogForm">
                                            <v-col style="padding-bottom: 0;" v-if="condition_field(field)" :sm="field.sm" v-bind:key="key">
                                                <components :label="conditionLabel(field)" :rows="field.rows"
                                                    :rules="field.rules" :readonly="field.readonly"
                                                    :disabled="field.disabled" :is="field.fieldtype"
                                                    :error_message="field.error_message" :outlined="field.outlined"
                                                    :maxdate="field.maxdate_field ? $store.state.Dialog.DialogForm.filter(obj => { return obj.dbfield == field.maxdate_field && obj.fieldtype == 'DateField' })[0].value : field.maxdate"
                                                    :mindate="field.mindate_field ? $store.state.Dialog.DialogForm.filter(obj => { return obj.dbfield == field.mindate_field && obj.fieldtype == 'DateField' })[0].value : field.mindate"
                                                    :field="field" :itemtext="field.itemtext" :itemvalue="field.itemvalue"
                                                    :dropdownitems="field.valuelist" :type="field.type">
                                                </components>
                                            </v-col>
                                        </template>
                                    </v-row>
                                </v-form>
                            </v-card-text>
                        </v-window-item>
                        <v-window-item :value="2">
                            <v-card-text>
                                <Success class="d-flex justify-center"></Success>
                                <h2 class="text-center">{{ success_message }}</h2>
                            </v-card-text>

                        </v-window-item>
                        <v-window-item :value="3">
                            <v-card-text class="d-flex justify-center">
                                <Failed></Failed>
                            </v-card-text>
                        </v-window-item>
                    </v-window>

                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <template>
                            <Button :text="true" color="default" title="Close" click="CloseDialog" :options="{}" />
                            <Button v-if="$store.state.Dialog.DialogWindow == 1"
                                @success="success" @error="handleError"
                                :text="$store.state.Dialog.SubmitButton.text"
                                :color="$store.state.Dialog.SubmitButton.color"
                                :title="$store.state.Dialog.SubmitButton.title"
                                :click="$store.state.Dialog.SubmitButton.click"
                                :options="{
                                    refs: $refs,
                                    validate_form: true,
                                    validate_form_name: $store.state.Dialog.RefName,
                                    data: getPostData(),
                                    custom_action: getCustomAction()
                                }"/>&nbsp;&nbsp;&nbsp;
                        </template>
                    </v-card-actions>
                </v-card>
                <components v-else :is="$store.state.Dialog.FormName"></components>
            </v-dialog>
        </div>
    </div>
</template>

<script>
// Common Imports in the mixin
import { ModuleImport } from '@/mixins/ModuleImport'

import { status_color, exception_rest_api_handler } from '@/helper'
import { bus } from '@/main';

export default {
    mixins: [ModuleImport],
    props: {
        disabled: { default: false },
    },
    beforeDestroy() {
        // Your code here
        console.log('Component is about to be destroyed.');
    },
    computed: {
        dialog () {
            return this.$store.state.Dialog.Dialog;
        },

        dialogWindow () {
            return this.$store.state.Dialog.DialogWindow;
        }
    },
    watch: {
        dialog () {
            this.error_message = '';
        },

        dialogWindow (value) {
            if (value === 2) {
                setTimeout(() => {
                    this.closeSuccessInfo()
                },  2000)
            }
        }
    },
    data: () => ({
        form: false,
        step: 1,
        success_message: "",
        error_message: ''
    }),
    created() {
        this.step = 1
    },
    mounted() {
        this.step = 1
    },
    methods: {
        condition_field(field) {
            if (field.fieldtype == 'Hiden') {
                return false
            }
            if (field.conditionfield && field.conditionfield1) {
                return (
                    this.$store.state['Dialog'].DialogForm.filter(obj => {
                        return obj.dbfield == field.conditionfield && String(obj.value) == String(field.conditionvalue)
                    }).length == 1 &&
                    this.$store.state['Dialog'].DialogForm.filter(obj => {
                        return obj.dbfield == field.conditionfield1 && String(obj.value) == String(field.conditionvalue1)
                    }).length == 1
                )
            } else if (field.conditionfield) {
                return (
                    this.$store.state['Dialog'].DialogForm.filter(obj => {
                        return obj.dbfield == field.conditionfield && String(obj.value) == String(field.conditionvalue)
                    }).length == 1
                )
            } else {
                return true
            }
        },

        success(click, api_response) {
            if (api_response && api_response.data && api_response.data.App && api_response.data.App == 'Team') {
                this.$store.dispatch('CloseDialog')
                this.$store.dispatch('TeamResourceStore/GET_TeamNameDetails', '?id=' + api_response.data.id)
                this.$store.dispatch('Snackbar', {
                    bar: true,
                    color: status_color(api_response.status),
                    text: 'Team ' + api_response.data.team_name + ' Added',
                })
                this.$store.state.Drawer.DrawerForm.filter(obj => { return obj.name == 'Team' })[0].value = api_response.data.id
                this.$store.dispatch('DisableDrawerLoader')
            }
            else if (api_response && api_response.data && api_response.data.App && api_response.data.App == 'Resoruce') {
                this.$store.dispatch('CloseDialog')
                this.$store.dispatch('Snackbar', {
                    bar: true,
                    color: status_color(api_response.status),
                    text: 'Resource ' + api_response.data.resource_name +'('+api_response.data.resource_id+')'+ ' Updated',
                })
                this.$store.dispatch('DisableDrawerLoader')
                bus.$emit('resource_update', api_response, this.$store.state['Dialog'].FormName, this.$store.state['Dialog'].DialogEditType,
            )
            }
            else if (api_response && api_response.data && api_response.data.App && api_response.data.App == 'Timesheet') {
                this.$store.dispatch('DialogChangeWindow', 2)
                this.success_message = api_response.data.message
                this.$store.dispatch('DisableDrawerLoader')
            }
            else if (api_response && api_response.data && api_response.data.App && api_response.data.App == 'TimeSheetApproval') {
                this.$store.dispatch('CloseDialog')
                this.$store.dispatch('Snackbar', {
                    bar: true,
                    color: status_color(api_response.status),
                    text: api_response.data.message,
                })
            }
            else if (api_response && api_response.data && api_response.data.App && api_response.data.App == 'ProjectVerification') {
                console.log('refresh issue');                
                this.$store.dispatch('CloseDialog')
                this.$store.dispatch('Snackbar', {
                    bar: true,
                    color: status_color(api_response.status),
                    text: 'Project ' + api_response.data.data.name + ' Approved Successfully ...',
                })
                this.$router.push({ name: 'Project' })
            }
            else if (api_response && api_response.data && api_response.data.App && api_response.data.App == 'FinanceTabExpense') {
                this.$store.dispatch('CloseDialog')
                this.$store.dispatch('Snackbar', {
                    bar: true,
                    color: status_color(api_response.status),
                    text: api_response.data.name + ' Added Successfully ...',
                })
            }
            else {
                this.$store.dispatch('CloseDialog')
            }
            bus.$emit(
                'form_success',
                api_response,
                this.$store.state['Dialog'].FormName,
                this.$store.state['Dialog'].DialogEditType,
            )

        },

        conditionLabel(field) {
            if (!field.conditioncheck) {
                return field.name
            } else {
                if (field.conditionfield) {
                    const chekValue = this.$store.state['Dialog'].DialogForm.filter(obj => {
                        return obj.dbfield == field.conditionfield && String(obj.value) == String(field.conditionvalue)
                    }).length == 1
                    return chekValue && field.conditionlabel ? field.conditionlabel : field.name
                } else {
                    const chekValue = this.$store.state['Dialog'].DialogForm.filter(obj => {
                        return obj.dbfield == field.conditionfield1 && String(obj.value) == String(field.conditionvalue1)
                    }).length == 1
                    return chekValue && field.conditionlabel ? field.conditionlabel : field.name
                }
            }
        },

        handleError (click, response) {
            const data = exception_rest_api_handler(response);
            this.error_message = data;
        },

        closeSuccessInfo () {
            this.$store.dispatch('CloseDialog', {});
        },

        openNewLogForm () {
            this.$store.dispatch('CloseDialog', {})
            this.$store.dispatch('OpenDialogOnClick', {
                Dialog: true,
                Title: 'Log Multiple',
                DialogMutation: 'mutation__dialog',
                DialogExtraParam: ``,
                API_FORM: false,
                DialogEditType: 'new',
                DialogWindow: '1',
                FormName: 'LogTimeForm',
                DialogSize: '800',
                SubmitButton: {
                    title: 'Submit',
                    text: true,
                    color: 'success',
                    click: 'appsStore/timesheetStore/Timesheet_API_Timesheet_Entry_Create',
                    extraParam: ``,
                    custom_action: `/multiple_log_entry`,
                    not_execute_extract: true
                }
            })
        },

        getPostData() {
            if (
                this.$store.state.Dialog.FormName === 'NewTeam' ||
                this.$store.state.Dialog.Title === 'New Milestone'
            ) {
                const project = localStorage.getItem('newProjectID')
                const data = [...this.$store.state.Dialog.DialogForm];
                const index = data.findIndex(ele => { return ele.dbfield === 'project_details'})
                data[index].value = project
                return data;
            } else {
                return this.$store.state.Dialog.DialogForm;
            }
        },

        getCustomAction() {
            if (
                this.$store.state.Dialog.FormName === 'Finance_Planned_Cost' &&
                !this.$route.params.pid
            ) {
                const project = localStorage.getItem('newProjectID')
                return `${project}/add_planned_expense`
            } else {
                return this.$store.state.Dialog.SubmitButton.custom_action
            }
        }

    },
}
</script>

<style scoped>

</style>


