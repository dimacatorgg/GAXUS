<script setup>
import { defineEmits,watch,ref, watchEffect,computed } from 'vue';
const emit = defineEmits(["ko"]);
import axios  from 'axios';
const props = defineProps({
    pro:Boolean,
    user:String,
})
function klik(){
    emit("ko",!props.pro)
}
const podaci = ref('');

const prijatelji = ref(false);
const userRef = computed(() => props.user);
watch(userRef, (newVal) => {
    axios.get(`http://localhost:8000/api/sigma/?user=${newVal}`).then(res => {podaci.value=res.data.message;
   
    }).catch(err => console.log(err))
    axios.get(`http://localhost:8000/api/check/?user1=${JSON.parse(localStorage.getItem("user")).name}&user2=${props.user}`).then(res => {
        if(res.data.message >0){
            prijatelji.value = true
        }
    }).catch(err => console.log(err))
});

</script>
<template>
   
    <div class="korisnik"  :class="{ac:props.pro}">
        <div class="rel" v-if="props.pro">
            <div @click="klik" class="backg">X</div>
            <div class="profik">
                <div class="img">
                    <img src="/src/;ambda.png" width="60px" height="60px">
                </div>
                <div class="name">{{ props.user }}</div>
                <div v-if="podaci">
                    <div class="gmail">{{ podaci.gmail }}</div>
                    <div v-if="prijatelji">
                        
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>