<template>
  <div>
    <v-app-bar color="primary" app dark>
      <v-app-bar-nav-icon @click.stop="switchShowDrawer">
        <v-icon>menu</v-icon>
      </v-app-bar-nav-icon>
      <v-app-bar-title>Bierlijst</v-app-bar-title>

      <v-spacer></v-spacer>
    </v-app-bar>

    <v-navigation-drawer persistent v-model="showDrawer" fixed app>
      <v-list dense nav>
        <v-subheader>Main menu</v-subheader>
        <v-list-item to="/main/dashboard">
          <v-list-item-icon>
            <v-icon>web</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Dashboard</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <v-divider></v-divider>

      <v-list dense nav>
        <v-subheader>Profile</v-subheader>

        <v-list-item to="/main/profile/view">
          <v-list-item-icon>
            <v-icon>person</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Show Profile</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item to="/main/profile/edit">
          <v-list-item-icon>
            <v-icon>edit</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Edit Profile</v-list-item-title>
          </v-list-item-content>
        </v-list-item>

        <v-list-item to="/main/profile/password">
          <v-list-item-icon>
            <v-icon>vpn_key</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Change Password</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <v-spacer></v-spacer>

      <template v-slot:append>
        <v-list dense nav>
          <v-list-item @click="logout">
            <v-list-item-icon>
              <v-icon>close</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>Logout</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </template>
    </v-navigation-drawer>

    <v-main>
      <router-view></router-view>
    </v-main>
    <v-footer class="pa-1" fixed app padless>
      <v-spacer></v-spacer>
      <span>ICheered</span>
    </v-footer>
  </div>
</template>

<script lang='ts'>
import { Vue, Component } from "vue-property-decorator";

import { dispatchUserLogOut } from "@/store/main/actions";

import { commitSetDashboardShowDrawer } from "@/store/main/mutations";

import { readDashboardShowDrawer } from "@/store/main/getters";

const routeGuardMain = async (to: any, from: any, next: any) => {
  console.log(to.path);

  if (to.path === "/main") {
    next("/main/home");
  } else {
    next();
  }
};

@Component
export default class Main extends Vue {
  public unreadNotifications: number = 0;

  public beforeRouteEnter(to: any, from: any, next: any) {
    routeGuardMain(to, from, next);
  }

  public beforeRouteUpdate(to: any, from: any, next: any) {
    routeGuardMain(to, from, next);
  }

  get showDrawer() {
    return readDashboardShowDrawer(this.$store);
  }
  set showDrawer(value: any) {
    commitSetDashboardShowDrawer(this.$store, value);
  }

  public switchShowDrawer() {
    commitSetDashboardShowDrawer(
      this.$store,
      !readDashboardShowDrawer(this.$store),
    );
  }

  public async logout() {
    await dispatchUserLogOut(this.$store);
  }
}
</script>
