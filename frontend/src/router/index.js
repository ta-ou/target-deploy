import Vue from "vue";
import VueRouter from "vue-router";

import Home from "@/views/Home.vue";
import NotFound from "@/views/NotFound.vue";
import OwnTarget from "@/views/OwnTarget.vue";
import Target from "@/views/Target.vue";
import TargetEditor from "@/views/TargetEditor.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
  },
  {
    path: "/target/:slug",
    name: "target",
    component: Target,
    props: true,
  },
  {
    path: "/set",
    name: "target-editor",
    component: TargetEditor,
  },
  {
    path: "/owntarget",
    name: "own-target",
    component: OwnTarget,
  },
  {
    path: "*",
    name: "page-not-found",
    component: NotFound,
  },
];

const router = new VueRouter({
  mode: "history",
  routes,
});

export default router;
