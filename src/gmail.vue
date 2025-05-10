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
watchEffect(() => {
    if( inputs.value!=null){
    console.log(inputs.value[0].value)
    }
})
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
            </div>
        </div>
    </div>
</template>