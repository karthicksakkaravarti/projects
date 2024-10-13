<!-- src/views/Documents.vue -->

<template>
    <v-container>
        <Button class="mt-0 mr-2" :outlined="true" :rounded="true" mdi_icon="mdi-plus" click="OpenDrawerOnClick"
            title="Create " tooltip="Create" :options="{
                ShowAppBarOnDrawer: true,
                DrawerSize: '30%',
                DrawerFormType: 'documents',
                DrawerFormTitle: 'Create',
                DrawerAddons: '/addons/apps/documents/api/documents',
                DrawerFormAPICall: true,
                DrawerFilterForm: false,
                DrawerMutation: 'mutation__drawer',
                DrawerExtraParam: `&project=${pid}`,
                DrawerActionType: 'new',
                DrawerFormSubmit: {
                    btn_name: 'Create Document',
                    store_action_name: 'DocumentsStore/CREATE_DOCUMENT',
                    custom_action: '',
                    data: '',
                },
            }" />
                    <v-btn  rounded outlined small color="primary" class="ml-2" @click="fetchDocuments"><v-icon>mdi-refresh</v-icon></v-btn>

        <div class="mt-2">
            <v-list>
                <v-list-item v-for="doc in documents" :key="doc.id">
                    <v-list-item-content>
                        <v-list-item-title>{{ doc.title }}                         <v-chip small># {{ doc.category }}</v-chip>                        </v-list-item-title>
                        <v-list-item-subtitle>By {{ doc.created_by }} on {{ formatDate(doc.created_at)
                            }}</v-list-item-subtitle>
                            
                    </v-list-item-content>
                    <!-- Acvvtion delete -->
                    <v-list-actions>
                        <!-- View -->
                        <v-btn color="primary" icon @click="viewDocument(doc.id)">
                            <v-icon>mdi-eye</v-icon>
                        </v-btn>
                        <!-- Delete -->
                        <v-btn color="error" icon @click="deleteDocument(doc.id)">
                            <v-icon>mdi-delete</v-icon>
                    </v-btn>
                 </v-list-actions>
                </v-list-item>
                <!-- If no documents -->
                <v-list-item v-if="documents.length === 0">
                    <v-list-item-title>No documents found</v-list-item-title>
                </v-list-item>
            </v-list>
        </div>

    </v-container>
</template>

<script>
import store from '@/store'
import { ModuleImport } from '@/mixins/ModuleImport'
import { bus } from '@/main'

export default {
    data() {
        return {
            documents: [],
        };
    },
    mixins: [ModuleImport],
    props: {
        pid: {
            type: String,
            required: false
        }
    },
    methods: {
        async fetchDocuments() {
            try {
                store
                    .dispatch('DocumentsStore/GET_DOCUMENTS', `?project=${this.pid}`)
                    .then(data => {
                        this.documents = data.data.results
                    })
                    .catch(err => {
                        console.error(err)
                    })

            } catch (error) {
                console.error('Error fetching documents:', error);
                // Handle error (e.g., redirect to login)
            }
        },
        async deleteDocument(id) {
            store.dispatch('DocumentsStore/DELETE_DOCUMENT', id)
            .then(data => {
                this.fetchDocuments()
            })
            .catch(err => {
                console.error(err)
            })
        },
        viewDocument(id) {
            this.$router.push({ name: 'document', params: { id } });
        },
        formatDate(dateStr) {
            const date = new Date(dateStr);
            return date.toLocaleDateString() + ' ' + date.toLocaleTimeString();
        },
    },
    created() {
        this.fetchDocuments();
        bus.$on('form_success', (response, form_name, form_type = null) => {
            console.log(response, form_name, form_type)
            this.$store.dispatch('CloseDrawer')

            this.fetchDocuments()
        })
    },
};
</script>