<template>
  <div id="app">
    <v-app>
      <v-main v-if="loggedIn === null">
        <v-container class="fill-height" fluid>
          <v-row align="center" justify="center">
            <v-col cols="12" sm="8" md="4">
              <div class="headline my-5">Loading...</div>
              <v-progress-circular
                size="100"
                indeterminate
                color="primary"
              ></v-progress-circular>
            </v-col>
          </v-row>
        </v-container>
      </v-main>
      <router-view v-else />
    </v-app>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import { readIsLoggedIn } from "@/store/main/getters";
import { dispatchCheckLoggedIn } from "@/store/main/actions";

@Component
export default class App extends Vue {
  get loggedIn() {
    return readIsLoggedIn(this.$store);
  }

  public async created() {
    await dispatchCheckLoggedIn(this.$store);
  }
}
</script>