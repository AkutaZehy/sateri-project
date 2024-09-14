import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Disk from "../views/Disk.vue";

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/disk/:side',
    name: 'Disk',
    component: Disk,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;