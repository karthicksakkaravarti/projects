<!-- src/views/DocumentEditor.vue -->

<template>
        <v-form @submit.prevent="saveDocument" v-if="document && document.id">
            <v-text-field v-model="document.title" label="Title" required></v-text-field>
            <WYSIWYG :field="field" />
            <v-divider></v-divider>
            <v-btn type="submit" class="mt-2" color="success">Update</v-btn>
        </v-form>
</template>

<script>
import store from '@/store'
import { ModuleImport } from '@/mixins/ModuleImport'

export default {
    mixins: [ModuleImport],
    data() {
        return {
            document: {},
            categories: [],
            field: {
                value: ""

            }
            
        };
    },
    props: {
        documentID: {
            type: String,
            required: true
        }
    },
    methods: {
        async getDocument() {
            store
                    .dispatch('DocumentsStore/GET_DOCUMENTS', this.documentID)
                    .then(data => {
                        this.document = data.data
                        this.field.value = this.document.content
                    })
                    .catch(err => {
                        console.error(err)
                    })
        },
        async saveDocument() {
            try {
                store
                    .dispatch('DocumentsStore/PATCH_DOCUMENT', {
                        id: this.documentID,
                        data: {
                            'content': this.field.value
                        }
                    })
                    .then(data => {
                        this.documents = data.data.results
                        store.dispatch('Snackbar', {
                        bar: true,
                        text: 'Updated',
                        })
                    })
                    .catch(err => {
                        console.error(err)
                    })
            } catch (error) {
                console.error('Error saving document:', error);
            }
        },
    },
    created() {
        this.getDocument();
    },
};
</script>