<template>
  <div>
    <!-- User info Component -->
    <v-list>
      <v-list-item>
        <Avatar :size="AvatarSize" :ShowPicChange="ShowPicChange"> </Avatar>

        <v-list-item-content class="ml-4">
          <v-list-item-title>{{$store.state.user.name}}</v-list-item-title>
          <v-list-item-subtitle>({{$store.state.user.username}})</v-list-item-subtitle>
        </v-list-item-content>

        <v-list-item-action> </v-list-item-action>
      </v-list-item>
    </v-list>
  </div>
</template>

<script>
import Avatar from "@/components/Users/Avatar.vue";
export default {
  props: {
    AvatarSize: {},
    ShowPicChange: {default: false}
  },
  components: {
    Avatar,
  },
};
</script>

<style>
</style>