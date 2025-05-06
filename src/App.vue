<script setup>

import {ref,computed, reactive} from 'vue'
import Footer from './Footer.vue';
import Task from './Task.vue';
import Background from './Background.vue';
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

function gh(){
  if(faza.value==list.value.length){
    lol.value=false;
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

}
/*setInterval(function(){
 

},500)*/

</script>
<template>
 <div class="center">
  <div class="rcenter">

  <form action="" @submit.prevent v-if="lol">
    
    <div class="input"><input type="text" v-model="input" :class="{ac:bools}" :placeholder="list[faza][2]">
      <span class="title" >{{ list[faza][1] }}</span></div>
      <div class="btns">
        
        <button class="back" :class="{ac : jelje}" @click="prev"><span>🠠</span></button>
        <button class="next" :class="{ac : jelje,bn:bools}" @click="gh"><span>Next</span></button>
    
      </div>
   
  </form>
  <div v-else class="sup">
    You are done now go check gmail and verify you self!
  </div>
  </div>
 </div>
 <Task></Task>
 <Background></Background>
</template>