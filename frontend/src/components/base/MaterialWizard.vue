<template>
  <v-card class="v-card--wizard" elevation="12" max-width="700">
    <v-card-title class="text-h1"> Add new device </v-card-title>

    <div class="text-center text-h4 grey--text font-weight-light mb-6" />

    <v-tabs
      ref="tabs"
      v-model="internalValue"
      background-color="#303030"
      color="white"
      grow
      slider-size="50"
    >
      <v-tabs-slider class="mt-1" color="primary" />

      <v-tab
        v-for="(item, i) in items"
        :key="i"
        :ripple="false"
        :disabled="!availableSteps.includes(i)"
      >
        {{ item }}
      </v-tab>
    </v-tabs>

    <div class="my-6" />

    <v-card-text>
      <v-tabs-items v-model="internalValue">
        <slot />
      </v-tabs-items>
    </v-card-text>

    <v-card-actions class="pb-4 pa-4">
      <v-btn
        :disabled="internalValue === 0"
        class="white--text"
        color="grey darken-2"
        min-width="125"
        large
        @click="$emit('click:prev')"
      >
        Previous
      </v-btn>

      <v-spacer />

      <v-btn
        class="white--text"
        color="error"
        min-width="100"
        large
        @click="$emit('click:cancel')"
      >
        Cancel
      </v-btn>

      <v-spacer />

      <v-btn
        :disabled="!availableSteps.includes(internalValue + 1)"
        color="success"
        min-width="100"
        large
        @click="$emit('click:next')"
      >
        {{ internalValue === items.length - 1 ? "Create" : "Next" }}
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
// Mixins
import Proxyable from "vuetify/lib/mixins/proxyable";

export default {
  name: "BaseMaterialWizard",

  mixins: [Proxyable],

  props: {
    availableSteps: {
      type: Array,
      default: () => [],
    },
    items: {
      type: Array,
      default: () => [],
    },
  },
};
</script>

<style lang="sass">
.v-card--wizard
  overflow: visible

  .v-tabs-bar
    height: 56px
    padding: 0 8px

    .v-tabs-slider-wrapper
      overflow: visible

    .v-tabs-slider
      border-radius: 4px

    .v-tabs-slider-wrapper
      contain: initial
      z-index: 0
</style>
