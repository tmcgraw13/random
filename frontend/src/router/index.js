import { createRouter, createWebHistory } from 'vue-router';
import Home from '../components/Home.vue';
import About from '../components/About.vue';
import News from '../components/News.vue';
import Contact from '../components/Contact.vue';


const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/about',
    name: 'About',
    component: About,
  },
  {
    path: '/contact',
    name: 'Contact',
    component: Contact,
  },
  {
    path: '/news',
    name: 'News',
    component: News,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
