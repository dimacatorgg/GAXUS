import { createRouter,createWebHistory } from "vue-router";
import Home from "./Home.vue";
import gmail from "./gmail.vue";
import Gmail from "./gmail.vue";
const routes = [
    { path: '/', component: Home },
    { path: '/about', component: Gmail },
  ];
  
  const router = createRouter({
    history: createWebHistory(),
    routes, 
  });
  
  export default router;
