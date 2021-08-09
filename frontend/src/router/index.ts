import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      component: () => import(/* webpackChunkName: "start" */ "@/views/main/Start.vue"),
      children: [
        {
          path: "login",
          // route level code-splitting
          // this generates a separate chunk (about.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          component: () => import(/* webpackChunkName: "login" */ "@/views/Login.vue"),
        },
        {
          path: "main",
          component: () => import(/* webpackChunkName: "main" */ "@/views/main/Main.vue"),
          // children: [
          // {
          //   path: "profile",
          //   component: RouterComponent,
          //   redirect: "profile/view",
          //   children: [
          //     {
          //       path: "view",
          //       component: () => import(
          //         /* webpackChunkName: "main-profile" */ "./views/main/profile/UserProfile.vue"),
          //     },
          //     {
          //       path: "edit",
          //       component: () => import(
          //         /* webpackChunkName: "main-profile-edit" */ "./views/main/profile/UserProfileEdit.vue"),
          //     },
          //     {
          //       path: "password",
          //       component: () => import(
          //         "./views/main/profile/UserProfileEditPassword.vue"),
          //     },
          //   ],
          // },
          // ],
        },
      ],
    },
    {
      path: "/*", redirect: "/",
    },
  ],
});
