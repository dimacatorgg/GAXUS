<script setup>
import register from './funckije';
import {ref,computed, reactive,onMounted} from 'vue'
import Footer from './Footer.vue';
import Task from './Task.vue';
import Background from './Background.vue';
import gmail from './gmail.vue';
import { useRouter ,useRoute} from 'vue-router';
import axios from 'axios';
const input = ref('');
const bools = computed(() => {
  return input.value!="" ? true : false
})

const listram = ref('')
const list = ref([['',"Username",'Enter Username'],['',"Password",'Enter your password'],['','Gmail','Please Enter your email here']])
const faza = ref(0);
const lol = ref(true);
const jelje = computed(() => {
  return faza.value > 0 ? true : false;
})






const podaci = ref(null)






const r = useRoute()

if(r.params.id=="1"){
  list.value.pop();
  console.log("Hej")
}











   function  gh(){
  if(faza.value==list.value.length){
    lol.value=false;
   // console.log(register(list[0][0],list[1][0],list[2][0]))
   if(r.params.id!="1"){





  axios.get(`http://localhost:8000/api/register/?name=${list.value[0][0]}&gmail=${list.value[2][0]}&password=${list.value[1][0]}`,{
    withCredentials:true,
  }).then(res => {
    console.log(res.data.message)
  }).catch(err => {
    console.log(err)
  })
}else{
  axios.get(`http://localhost:8000/api/login/?name=${list.value[0][0]}&password=${list.value[1][0]}`).then(res => {
    console.log("Uspesno si se ulogovao")
  }).catch(err => {
    console.log(err)
  })
}

  }else{
  if(bools){
    list.value[faza.value][0] = input.value;
    faza.value++;
    input.value = list.value[faza.value][0];
  }
}
}
function prev(e){
  if(faza.value >0){
    list.value[faza.value][0] = input.value;
  
    faza.value--;
    input.value = list.value[faza.value][0];
  
  }
  else{
    alert("Monckz sta radis")
  }
}
function anim(){
  register()
}
/*setInterval(function(){
 

},500)*/

</script>
<template>

 <div class="center">
  <div class="rcenter">

  <div v-if="lol">
    
    <div class="input"><input type="text" v-model="input" :class="{ac:bools}" :placeholder=list[faza][2] required>
      <span class="title" >{{ list[faza][1] }}</span></div>
      <div class="btns">
        
        <button class="back" :class="{ac : jelje}" @click="prev"><span>🠠</span></button>
        <button class="next" :class="{ac : jelje,bn:bools}" @click="gh" type="submit"><span>Next</span></button>
    
      </div>
   
    </div>
  <div v-else class="sup">
   <h2>Hej</h2>
  </div>
  </div>
 </div>

 <Background></Background>

</template>