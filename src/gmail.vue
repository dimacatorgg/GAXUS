<script setup>
import {ref,computed,watch} from "vue"
    const vrednsoti = ref(["","","","","",""]);
    const active = ref([0])
  
  
       /* vrednsoti.value.forEach((item,index) => {
        watch(item,(s) => {
           active.value[0] = index;
           console.log(index);
        })
    })

for(var i = 0;i<vrednsoti.value.length;i++){
    watch(vrednsoti.value[i],() =>{
        active.value[0] = i;
    })
}*/
const some = ref(-1);
setInterval(function(){
    for(var i=0;i<document.querySelectorAll("input").length;i++){
    if(document.querySelectorAll("input")[i] === document.activeElement){
        some.value = i;
    }
}
},100)

   window.onkeyup = function(){
        console.log(some.value)
   }
</script>




<template>

    <div class="body-center">
        <div class="rel">
            <div class="form">
                <div class="title">
                    Please Enter code which we sent to you,check gmail.
                </div>
                <!--<div class="code">
                    <div class="codes">
                        <input >
                    </div>
                    <div class="codes">
                        <input>
                    </div>
                    <div class="codes">
                        <input>
                    </div>
                    <div class="codes">
                        <input>
                    </div>
                    <div class="codes">
                        <input>
                    </div>
                    <div class="codes">
                        <input>
                    </div>
                </div>-->
                <div class="code">
                 
                    <div class="codes" v-for="(code,index) in vrednsoti">
                        <input v-model="vrednsoti[index]" maxlength="1"/>
                       
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>