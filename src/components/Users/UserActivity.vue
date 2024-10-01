<template>
  <div>
    <div v-if="historyList.length > 0" class="ma-2">
      <div class="d-flex justify-end mb-2">
        <v-btn small color="primary">Export</v-btn>
      </div>
      <v-simple-table fixed-header height="900px">
        <template v-slot:default>
          <v-timeline dense class="timeline-custom-dense timeline-custom-dots" v-for="(history, index) in historyList"
            v-bind:key="index">
            <v-timeline-item color="error" small>
              <div class="d-flex justify-space-between align-center flex-wrap">
                <h4 class="font-weight-medium me-1">
                  <small class="text-no-wrap"></small> {{ history.activity.toUpperCase() }} - {{ history.activity_state }} {{ history.activity }} {{ history.comment }}
                </h4>
                
              </div>
              <p class="mb-0">
                {{ history.action_date }}
                 <!-- {{ history.activity_state }} {{ history.activity }} {{ history.comment }} -->
              </p>
            </v-timeline-item>
          </v-timeline>
        </template>
      </v-simple-table>


    </div>

    <div v-else>
      No actions.
    </div>
  </div>
</template>

<script>

export default {

  props: {
    historyList: {
      type: Array,
      default() {
        return [];
      }
    }
  }

}

</script>

<style></style>
