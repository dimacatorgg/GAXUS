import { createRouter,createWebHistory } from "vue-router";
import Home from "./Home.vue";
import gmail from "./gmail.vue";
import Gmail from "./gmail.vue";
import Juj from "./Juj.vue";
import Aplikacija from "./aplikacija.vue";
import Lista from "./Lista.vue";
import Test from "./test.vue";
const routes = [
    {path: '/',component:Juj},
    { path: '/register/:id', component: Home },
   
    {path:'/app/',component:Aplikacija},
    {path:'/friends',component:Lista},
    {path:'/test/',component:Test},
    {path:'/gmail/',component:Gmail}
  ];
  
  const router = createRouter({
    history: createWebHistory(),
    routes, 
  });
  
  export default router;
