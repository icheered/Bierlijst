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
              <h1 class="text-h3 font-weight-bold">Login</h1>
            </div>
          </template>

          <v-card-text class="text-center pt-10">
            <v-form @keyup.enter="submit">
              <v-text-field
                @keyup.enter="submit"
                v-model="username"
                prepend-icon="person"
                name="login"
                label="Login"
                type="text"
              ></v-text-field>
              <v-text-field
                @keyup.enter="submit"
                v-model="password"
                :append-icon="showpassword ? 'mdi-eye' : 'mdi-eye-off'"
                :type="showpassword ? 'text' : 'password'"
                @click:append="showpassword = !showpassword"
                prepend-icon="lock"
                name="password"
                label="Password"
              ></v-text-field>
            </v-form>

            <v-row justify="center" align="center" v-if="username != 'Sloth'">
              <v-switch v-model="rememberme"></v-switch>
              Remember me
            </v-row>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-hover v-slot="{ hover }">
                <v-btn
                  large
                  color="success"
                  :rounded="true"
                  :elevation="hover ? 8 : 2"
                  @click="submit"
                >
                  Let's Go
                </v-btn>
              </v-hover>
              <v-spacer></v-spacer>
            </v-card-actions>

            <div v-if="loginError">
              <v-alert
                :value="loginError"
                transition="fade-transition"
                type="error"
              >
                {{ loginError }}
              </v-alert>
            </div>
          </v-card-text>
        </base-material-card>
      </v-slide-y-transition>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import { readLoginError } from "@/store/main/getters";
import { dispatchLogIn } from "@/store/main/actions";
import { VBtn } from "vuetify/lib";

@Component({
  components: {
    VBtn,
  },
})
export default class Login extends Vue {
  public username: string = "";
  public password: string = "";
  public rememberme: boolean = true;
  public showpassword: boolean = false;

  public get loginError(): string {
    return readLoginError(this.$store);
  }

  public submit() {
    dispatchLogIn(this.$store, {
      username: this.username,
      password: this.password,
      rememberme: this.rememberme,
    });
  }
}
</script>

<style>
</style>
