import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Disk from "../views/Disk.vue";
import C from "../views/C.vue";
import Password from "../views/Password.vue";
import Instruction from "../views/Instruction.vue";
import Puzzle from "../views/Puzzle.vue";

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: {title: 'Home'}
  },
  {
    path: '/disk/:side',
    name: 'Disk',
    component: Disk,
    meta: {title: '光碟的 :side 面'}
  },
  {
    path: '/c',
    name: 'C-side',
    component: C,
    meta: {title: '光碟的 C 面'}
  },
  {
    path: '/password',
    name: 'Password',
    component: Password,
    meta: {title: '你发现了隐藏的页面！'}
  },
  {
    path: '/puzzle',
    name: 'Puzzle',
    component: Puzzle,
    meta: {title: '谜题'}
  },
  {
    path: '/instruction',
    name: 'Instruction',
    component: Instruction,
    meta: {title: 'Sateri Demo 使用说明'}
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;