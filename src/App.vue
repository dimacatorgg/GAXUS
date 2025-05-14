<script setup>
import { onMounted,ref } from 'vue';
import verification from './verif';
import { useRouter } from 'vue-router';
const router = useRouter();
const gg = ref(null)
onMounted(async () => {
  const data = await fetch(`http://localhost:8000/api/cockie/`);
  gg.value = await data.json()
 
  if(gg.value.message==""){
    router.push("/register")
    console.log("sdasd")
  }else {
  
    console.log(gg.value.message)
  }
})

</script>
<template>

<router-view></router-view>
</template>