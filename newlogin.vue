<template>
  <v-container id="login" class="fill-height justify-center" tag="section">
    <v-row justify="center">
      <v-slide-y-transition appear>
        <base-material-card
          color="primary"
          light
          max-width="100%"
          width="400"
          class="px-5 py-3"
        >
          <template v-slot:heading>
            <div class="text-center">
              <h1 class="text-h3 font-weight-bold mb-2">Login</h1>
            </div>
          </template>

          <v-card-text class="text-center">
            <v-text-field
              v-model="username"
              color="primary"
              label="Username..."
              prepend-icon="mdi-account"
              class="mt-10"
            />

            <v-text-field
              v-model="password"
              :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
              :type="showPassword ? 'text' : 'password'"
              class="mb-8"
              color="primary"
              label="Password..."
              prepend-icon="mdi-lock-outline"
              @click:append="showPassword = !showPassword"
            />

            <v-row justify="center" align="center" v-if="username != 'Sloth'">
              <v-switch v-model="rememberMe"></v-switch>
              Remember me
            </v-row>

            <v-row justify="center" align="center" class="pb-7" v-else>
              <h1 class="subtitle-2 font-weight-light">
                For security reasons I won't let you auto-signin using the
                master account
              </h1>
            </v-row>

            <pages-btn
              large
              color=""
              class="v-btn--text primary--text"
              v-if="isLoading"
            >
              <v-progress-circular
                indeterminate
                color="primary"
              ></v-progress-circular>
            </pages-btn>

            <pages-btn
              large
              color=""
              class="v-btn--text primary--text"
              @click="getSessionToken"
              v-else
            >
              Let's Go
            </pages-btn>
            <v-row
              justify="center"
              align="center"
              class="pt-5 mb-n4"
              v-if="showErrorText"
            >
              <h1 class="subtitle-1 red--text">{{ errorText }}</h1>
            </v-row>
          </v-card-text>
        </base-material-card>
      </v-slide-y-transition>
    </v-row>
  </v-container>
</template>

<script>
import { URLS } from "@/variables.js";
const querystring = require("querystring");

export default {
  name: "PagesLogin",

  components: {
    PagesBtn: () => import("./components/Btn"),
  },
  data() {
    return {
      showPassword: false,
      rememberMe: false,
      errorText: "",
      showErrorText: false,
      username: "",
      password: "",
      isLoading: false,
    };
  },
  methods: {
    getSessionToken() {
      console.log("Getting session token");
      this.isLoading = true;

      let URL = URLS.ORCA + "/api/auth/auth/?";
      URL += "name=" + this.username;
      URL += "&password=" + this.password;

      fetch(URL, {})
        .then((response) => response.json())
        .then((data) => {
          this.onTokenCallback(data);
        })
        .catch((error) => {
          console.error("Error: ", error);
          this.errorText = "The authentication server is not responding";
          this.showErrorText = true;
          this.isLoading = false;
        });
    },
    onTokenCallback(response) {
      // Parse the return info, store token if succesful
      //console.log(response)
      if (response.type == "response") {
        if (response.payload.status == "success") {
          this.$store.commit("SET_SESSION_TOKEN", response.payload.token);

          this.$store.dispatch("startWSConnection");

          this.$store.commit("SET_USERNAME", this.username);
          if (this.username == "Sloth") {
            this.$router.push("/register", () => {});
          } else {
            this.$router.push("/dashboard", () => {});
          }
        } else if (response.payload.status == "fail") {
          console.log(response.payload.reason);
          this.errorText = response.payload.reason;
          this.showErrorText = true;
          this.isLoading = false;
        }
      } else {
        console.log("Nay");
      }
    },
  },
};
</script>
