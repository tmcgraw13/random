import { createRouter, createWebHistory } from 'vue-router';
import Games from '@/views/Games.vue';
import Home from '@/views/Home.vue';
import Contact from '@/views/Contact.vue';
import News from '@/views/News.vue';
import About from '@/views/About.vue';


const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/news',
    name: 'News',
    component: News,
  },
  {
    path: '/contact',
    name: 'Contact',
    component: Contact,
  },
  {
    path: '/games',
    name: 'Games',
    component: Games,
  },
  {
    path: '/about',
    name: 'About',
    component: About,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
