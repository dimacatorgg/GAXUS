<script setup>
import {ref,watch,computed,onMounted} from "vue";
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
            console.log(document.querySelectorAll(".hs")[index])
        }else{
            console.log("dasd")
        }
    }
    })
})
</script>

<template>
    <div class="apps">
        <div class="app-options">
            <div class="aleft">
                <div class="app-user">
                    <div class="hover"></div>
                    <div class="status">

                    </div>
                    <div class="name hs" @mouseenter="hover[0] = true" @mouseleave="hover[0] = false">
                        <img width="30px" height="30px" src="./May 5, 2025, 06_50_21 PM.png">Dimitrije
                    </div>
                    <div class="app-more">

                    </div>
                    <div class="verif hs" @mouseenter="hover[1]= true" @mouseleave="hover[1] = false">
                        <img width="40px" height="40px" src="/src/lol.png">
                    </div>
                </div>
            </div>
            <div class="app-center">12:00</div>
            <div class="aright">
                <div class="roptions">Settings</div>
                <div class="roptions">Explore</div>
                <div class="roptions">Competions</div>
            </div>
        </div>
    </div>
</template>