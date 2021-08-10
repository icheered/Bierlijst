import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      component: () => import("@/views/main/Start.vue"),
      children: [
        {
          path: "login",
          component: () => import("@/views/Login.vue"),
        },
        {
          path: "main",
          component: () => import("@/views/main/Main.vue"),
          children: [
            {
              path: "home",
              component: () => import("@/views/main/Home.vue"),
            },
          ],
        },
        {
          path: "/*", redirect: "/",
        },
      ],
    },
  ],
});
