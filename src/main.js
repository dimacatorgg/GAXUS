import './assets/main.css'
import './assets/app.css'
import './assets/mainj.css'
import './assets/fr.css'
import './assets/upitnik-removebg-preview.png'
import './assets/new.css'
import { createApp } from 'vue'
import App from './App.vue'
import { createPinia } from 'pinia'
import router from './router'
const app = createApp(App);
const pinisa = createPinia();

app.use(router);
app.use(pinisa);
app.mount("#app");

