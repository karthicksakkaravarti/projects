<template>
  <div>
    <v-card :style="`cursor: pointer; border-style: dotted;border-color: ${$vuetify.theme.themes.light.primary}`"
      :elevation="dragover ? 10 : 0" @dragover.prevent="dragover = true" @dragenter.prevent="dragover = true"
      @dragleave.prevent="dragover = false">
      <v-card-text class="ma-0 pa-1">
        <v-sheet @drop.prevent="onFileChanged($event)" id="dropzone" ref="dzone" tabindex="0"
          title="Click to grap a file from your PC!" color="lighten-4" width="100%" height="60" class="pa-2"
          @click="onClick">
          <v-file-input v-show="false" ref="upload" counter multiple show-size @change="onFileChanged"
            truncate-length="15"></v-file-input>

          <v-row justify="center">
            <v-icon v-if="!dragover" color="primary darken-2" size="40">mdi-cloud-upload-outline</v-icon>
            <v-icon v-if="dragover" color="primary darken-2" size="40">mdi-cloud-upload</v-icon>
          </v-row>
          <v-row justify="center">
            <span class="primary--text">Drag'n drop or click to upload file</span>
          </v-row>
        </v-sheet>
      </v-card-text>
      <!-- <v-fade-transition>
        <v-overlay v-if="hover" absolute color="#036358">
          <v-btn>See more info</v-btn>
        </v-overlay>
      </v-fade-transition> -->
    </v-card>
    <div id="files" v-if="files.length >= 1">
      <Section :label="label" />
      <v-data-table no-data-text="No Files Found" class="mt-2" dense :items="files" :headers="[
        { text: 'File', value: 'name' },
        { text: 'Tags', value: 'tag' },
        { text: 'Action', value: 'action' },
      ]">
        <template v-slot:item.action="{ item }">
          <v-icon color="primary" @click="removeFile(item.name)">mdi-trash-can-outline</v-icon>
        </template>
        <template v-slot:item.tag="{ item }">
          <v-combobox multiple class="ma-1" clearable  placeholder="Enter a tag and hit 'Enter' to confirm" dense hide-details  persistent-placeholder
            small-chips></v-combobox>
        </template>
      </v-data-table>
    </div>
  </div>
</template>

<script>
import Section from '@/components/Helpers/Section.vue'

export default {
  components: {
    Section,
  },
  props: {
    field: { default: {} },
    label: { default: 'Attachments' }
  },
  data() {
    return {
      dragover: false,
      files: [],
    }
  },
  methods: {
    onClick() {
      // this.$refs.upload.click()
      this.$refs.upload.$refs.input.click()
    },
    addFiles(files) {
      let formData = new FormData()

      for (var file of files) {
        this.files.push(file)
        console.log('-->', this.field)
        this.field.value.push(file)
        formData.append("filename", "Hellow");
      }
      // console.log(formData)
      // this.field.value = formData
    },
    onFileChanged(e) {
      this.dragover = false
      console.log(e)
      if (e) {
        try {
          this.addFiles(e)
        } catch (err) {
          err
        }
      }
      if (e.dataTransfer.files) {
        this.addFiles(e.dataTransfer.files)
      }

      // do something
    },
    removeFile(fileName) {
      const index = this.files.findIndex(file => file.name === fileName)
      // If file is in uploaded files remove it
      if (index > -1) this.files.splice(index, 1)
    },
  },
}
</script>

<style></style>