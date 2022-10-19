import { createRouter, createWebHistory } from 'vue-router';
import HelloWorld from '../components/HelloWorld.vue';
import Ping from '../components/Ping.vue';

const routes = [
  {
    path: '/',
    name: 'home',
    component: HelloWorld,
  },
  {
    path: '/ping',
    name: 'PingMe',
    component: Ping,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
