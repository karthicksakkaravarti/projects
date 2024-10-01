<template>
  <h3 :style="`border-left: 5px solid ${$vuetify.theme.themes.light.primary}`" class="pl-3 mt-3">{{label}}</h3>
</template>

<script>
export default {
    props: {
        label : {default: ''}
    }
}
</script>

<style>
</style>