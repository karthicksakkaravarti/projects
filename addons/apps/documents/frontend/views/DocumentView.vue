<!-- Document View -->

<template>
  <DocumentEditor :documentID="documentID" />
</template>

<script>
import { damp } from 'three/src/math/MathUtils.js';
import DocumentEditor from '../components/DocumentEditor.vue';

export default {
  name: 'DocumentView',
  components: {
    DocumentEditor
  },
  data() {
    return {
      document: {}
    }
  },
  created() {
    // get document by id
    this.documentID = this.$route.params.id;  
  },
};
</script>