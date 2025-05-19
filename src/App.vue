<script setup>
import { onMounted,ref } from 'vue';
import verification from './verif';
import axios from "axios"
import { useRouter } from 'vue-router';
const router = useRouter();
const gg = ref(false)

onMounted(() => {
   axios.get("http://localhost:8000/api/cockie/", {
  withCredentials:true
}).then(res => {
  if(res.data.message==""){
  console.log("Idi registruj se")
gg.value = false;
setTimeout(function(){
  if(localStorage.getItem("user")){
  localStorage.removeItem("user")
}
},3000)
  }else{
    console.log(res.data.message)
    gg.value = true;
  }
  
}).catch(err => {
  console.log(err)
})

  /*if(gg.value.message==""){
    router.push("/register")
    console.log(gg.value)
  }else {
  
    console.log(gg.value)
  }*/
})




</script>
<template>
 
<div :class="{'vidi':gg}" class="reistery">
  REgistruj se 
  <router-link to="register/1/">Register</router-link>
  <router-link to="register/5/">Login</router-link>

</div>
<router-view></router-view>
</template>