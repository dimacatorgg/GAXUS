<script setup>
import { onMounted } from 'vue';
import {ref} from "vue"
import axios from 'axios';
import { defineEmits } from 'vue';
const emit = defineEmits(["profil"],["prijatelj"]);
const poki = ref(null)
    onMounted(() => {
        setInterval(function(){
            axios.get(`http://localhost:8000/api/prijateljd/?user=${JSON.parse(localStorage.getItem("user")).name}`).then(res => poki.value = res.data.message).catch(err => console.log(err));
        },1000)
       
    });
function nesto(k){
    emit("profil",k)

}

</script>
<template>
    <div class="friends">
        <div class="lists col-80">
            <div class="podaci" v-if="poki==null">
                Loading
                <div class="dots">
                    <div class="dot"></div>
                    <div class="dot"></div>
                    <div class="dot"></div>
                </div>
            </div>
            <div class="kpodaci" v-else>
                <div class="friend" v-for="koki in poki">
                    <div class="fimg"><img src="/src/;ambda.png" width="35px" height="35px"></div>
                    <span class="fname">{{ koki.name }}</span>
                    <div class="info">
                        <div class="rel">
                            
                            <div class="bgs">
                                <span class="ibgs">
                                    <img src="/src/assets/ChatGPT_Image_May_23__2025__11_04_59_AM-removebg-preview.png" width="25px" height="25px">
                                </span>
                                <span class="itext" @click="nesto(koki.name)">Profile</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <router-link to="/friends/" class="col-20 bhj">No People here find some here</router-link>
     
    </div>

</template>