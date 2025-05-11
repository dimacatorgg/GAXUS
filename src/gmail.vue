<script setup>
import {ref,computed,watch,watchEffect} from "vue"
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
const inputs = ref(null)
const vlls = ref(document.querySelectorAll("input"));
const some = ref(-1);
setInterval(function(){
    for(var i=0;i<document.querySelectorAll("input").length;i++){
    if(document.querySelectorAll("input")[i] === document.activeElement){
        some.value = i;
    }

}
},100)
setInterval(function(){
    if(inputs.value != null){
        inputs.value.forEach(item => {
            if(item.value!=""){
                item.parentElement.classList.add("active")
            }else{
                item.parentElement.classList.remove("active")
            }
        })
    }
},100)
   window.onkeyup = function(e){
    
        if(some.value>=0 && e.key!="Backspace" && some.value!=vrednsoti.value.length-1){
            if(document.querySelectorAll("input")[some.value].value != ""){
                document.querySelectorAll("input")[some.value +1].focus();
                
             //   document.querySelectorAll("input")[some.value +1].innerHTML = e.key;
            }
        }else if(some.value!=0 && e.key=="Backspace"){
            if(document.querySelectorAll("input")[some.value].value == ""){
                document.querySelectorAll("input")[some.value-1].focus();
               
            }
        }
   }
 
   const clock = ref(30);
   const clockr = ref(true)
 setInterval(function(){
    if(clockr.value == false){
        clearInterval(this)
    }else{
        clock.value-=1;
    }
 },1000)
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
                        <input v-model="vrednsoti[index]" maxlength="1"  ref="inputs" />
                       
                    </div>
                </div>
                <div class="clock">
                  <div class="tt">Code will expire for</div>
                    <div class="rclock">
                        <div class="rclocki">
                        {{ clock }}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>