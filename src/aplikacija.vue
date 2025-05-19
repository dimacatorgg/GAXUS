<script setup>
import {ref,watch,computed,onMounted, Static} from "vue";
import Settigns from "./Settigns.vue";
import Friends from "./Friends.vue";
const hover = ref([false,false])
watch(hover.value,function(novo) {
    novo.forEach((item,index) => {
        if(hover.value[0] == false && hover.value[1] == false){
            document.querySelectorAll(".hs")[0].parentElement.querySelector(".hover").style.background = "transparent";
        }else{
            document.querySelectorAll(".hs")[0].parentElement.querySelector(".hover").style.background = "linear-gradient(to right, #dad299, #b0dab9)";
        if(hover.value[index]){
            if(index==1){
                document.querySelectorAll(".hs")[0].parentElement.querySelector(".hover").style.left = 5 -document.querySelectorAll(".hs")[0].parentElement.getBoundingClientRect().left + document.querySelectorAll(".hs")[index].getBoundingClientRect().left + "px";
                document.querySelectorAll(".hs")[0].parentElement.querySelector(".hover").style.width = 30 + "px";
                document.querySelectorAll(".hs")[0].parentElement.querySelector(".hover").style.height =30 + "px";
            }else{
            document.querySelectorAll(".hs")[0].parentElement.querySelector(".hover").style.left =5 -document.querySelectorAll(".hs")[0].parentElement.getBoundingClientRect().left + document.querySelectorAll(".hs")[index].getBoundingClientRect().left + "px";
            document.querySelectorAll(".hs")[0].parentElement.querySelector(".hover").style.width = document.querySelectorAll(".hs")[index].offsetWidth + "px";
            document.querySelectorAll(".hs")[0].parentElement.querySelector(".hover").style.height = document.querySelectorAll(".hs")[index].offsetHeight + "px";
            }
 
        }else{
          
        }
    }
    })
})
const minute = ref(new Date().getMinutes());
const sate = ref(new Date().getHours());
const sigma = ref(null)

function dalije(x){
    if(x<10){
        return true;
    }else{
        return false;
    }
}
const podaci = JSON.parse(localStorage.getItem("user"));
console.log(podaci)
const nulaminuti = computed(() => {return minute.value < 10 ? true : false})
const nulasati = computed(() => {return sate.value <10 ? true : false})
onMounted(() => {
console.log(nulaminuti.value)

    setInterval(function(){
        if(minute.value+1==60){
            minute.value=0;
            if(sate.value+1==24){
                sate.value=0;
            }else{
                sate.value+=1;
            }
        }else{
            minute.value +=1;

        }
        
    },1000*60);
});

const si =ref(false);
</script>

<template>
    <div class="apps">
      <!-- <Settigns :klik="si"></Settigns>-->
        <div class="app-options">
            <div class="aleft">
                <div class="app-user">
                    <div class="hover"></div>
                    <div class="status">

                    </div>
                    <div class="name hs" @mouseenter="hover[0] = true" @mouseleave="hover[0] = false">
                        <img width="30px" height="30px" src="./May 5, 2025, 06_50_21 PM.png">
                        {{ podaci ? podaci.name : "Guest"}}
                    </div>
                    <div class="app-more">

                    </div>
                    <div class="verif hs" @mouseenter="hover[1]= true" @mouseleave="hover[1] = false">
                        <img width="40px" height="40px" src="/src/assets/upitnik-removebg-preview.png">
                    </div>
                </div>
            </div>
        <div class="app-center" ref="sigma"><span class="sati">{{nulasati ? "0" : ""}}{{ sate }}</span>:<span class="minuti">{{nulaminuti ? "0" : ""}}{{ minute}}</span></div>
            <div class="aright">
                <div class="roptions" @click="si = !si">Settings</div>
                <div class="roptions">Explore</div>
                <div class="roptions">Competions</div>
            </div>

        </div>
        <div class="dole">
            <Friends></Friends>
        </div>
    </div>
</template>