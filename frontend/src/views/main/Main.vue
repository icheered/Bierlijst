<template>
  <div>
    <v-app-bar color="primary" app dark>
      <v-app-bar-nav-icon @click.stop="switchShowDrawer">
        <v-icon>menu</v-icon>
      </v-app-bar-nav-icon>
      <v-app-bar-title>Bierlijst</v-app-bar-title>

      <v-spacer></v-spacer>

      <v-btn icon @click.stop="switchShowNotificationsDrawer">
        <v-badge
          :content="unreadNotifications"
          :value="unreadNotifications"
          color="red"
          overlap
        >
          <v-icon>notifications</v-icon>
        </v-badge>
      </v-btn>
    </v-app-bar>

    <v-navigation-drawer
      persistent
      :mini-variant="miniDrawer"
      v-model="showDrawer"
      fixed
      app
    >
      <v-list dense nav>
        <v-subheader v-show="!miniDrawer">Main menu</v-subheader>
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
        <v-subheader v-show="!miniDrawer">Profile</v-subheader>

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

          <v-list-item @click="switchMiniDrawer">
            <v-list-item-icon>
              <v-icon
                v-html="miniDrawer ? 'chevron_right' : 'chevron_left'"
              ></v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>Collapse</v-list-item-title>
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

const routeGuardMain = async (to: any, from: any, next: any) => {
  if (to.path === "/main") {
    next("/main/dashboard");
  } else {
    next();
  }
};

@Component
export default class Main extends Vue {
  public unreadNotifications: number = 0;
  private notificationUpdateHook: any | undefined = undefined;

  public beforeRouteEnter(to: any, from: any, next: any) {
    routeGuardMain(to, from, next);
  }

  public beforeRouteUpdate(to: any, from: any, next: any) {
    routeGuardMain(to, from, next);
  }

  public async beforeDestroy() {
    clearInterval(this.notificationUpdateHook);
  }

  public async logout() {
    await dispatchUserLogOut(this.$store);
  }
}
</script>
