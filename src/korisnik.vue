<script setup>
import { defineEmits,watch,ref, watchEffect,computed } from 'vue';
const emit = defineEmits(["ko"]);
import axios  from 'axios';
import { checkFriend } from './pinias/chekcfriend';
import { removefriend } from './pinias/removefriend';
const gr = removefriend();
const korisnik = computed(() => {
    return localStorage.getItem("user") ? JSON.parse(localStorage.getItem("user")) : ""
})
const props = defineProps({
    pro:Boolean,
    user:String,
})
function klik(){
    emit("ko",!props.pro)
}

const podaci = ref('');
const pup = checkFriend();
const prijatelji = ref(false);
const userRef = computed(() => props.user);

watchEffect(async () => {
    if(userRef){
    axios.get(`http://localhost:8000/api/sigma/?user=${userRef.value}`).then(res => {podaci.value=res.data.message;
   
    }).catch(err => console.log(err));
    prijatelji.value = await pup.checkg(JSON.parse(localStorage.getItem("user")).name,userRef.value)
}
   
});
function removes(k,g){
    gr.remove(k,g);
    console.log("unfriend");
    prijatelji.value = false;
}
</script>
<template>
   
    <div class="korisnik"  :class="{ac:props.pro}" >
        <div class="rel" v-if="props.pro">
            <div @click="klik" class="backg">X</div>
            <div class="profik">
                <div class="img">
                    <img src="/src/;ambda.png" width="60px" height="60px">
                </div>
                <div class="name">{{ props.user }}</div>
                <div v-if="podaci" style="display: flex;flex-direction: column; padding: 2px; flex-wrap: wrap;gap: 5px;">
                    <div class="gmail">{{ podaci.gmail }}</div>
                    <div class="hbo" v-if="prijatelji" @click="removes(korisnik.name,podaci.name)">Unfollow</div>
                    <div v-else class="hbo">Follow</div>
                </div>
            </div>
        </div>
    </div>
</template>