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
const lista = ref([])
const about = ref('')
const broj = ref(0)
watch(userRef,() => {
    
     axios.get(`http://localhost:8000/api/getabout/?name=${podaci.value.id}`).then(res => {
   if(res.data.message[0]){console.log(res.data.message);about.value =  res.data.message[0]}else{about.value="Nista"}
   }).catch(err => console.log(err))
  
})

watchEffect(async () => {
    if(userRef){
    axios.get(`http://localhost:8000/api/sigma/?user=${userRef.value}`).then(res => {podaci.value=res.data.message;broj.value+=1;
   
    
    
    
    
    }).catch(err => console.log(err));
    
    prijatelji.value = await pup.checkg(JSON.parse(localStorage.getItem("user")).name,userRef.value)
}
   
});
const nnovo = ref(0)
watch(broj, () => {
    lista.value = []
 
     axios.get(`http://localhost:8000/api/komentari/?idx=${podaci.value.id}`).then(res => {res.data.message ? lista.value = res.data.message : "";}).catch(err => console.log(err))
    
})
const prosek = ref(0)
watch(lista,() => {
  
})
function removes(k,g){
    gr.remove(k,g);
    console.log("unfriend");
    prijatelji.value = false;
}
const comacc = ref(null)
const rate = ref(null)
const kuj = ref(false)
function pisi(){
   axios.get(`http://localhost:8000/api/upisi/?id1=${podaci.value.id}&data=${comacc.value}&user=${korisnik.value.name}&rate=${rate.value}`).then(res => kuj.value = true).catch(err => console.log(err))
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
                    {{ about }}
                <div style="display: flex;flex-direction: column;">
                  <div v-for="joj in lista">
                    <span>{{ joj.ime }}</span>
                    <p>{{ joj.poruka }}</p>
                    <p>{{ joj.rate }}/10</p>
                    <br>
                  </div>
                </div>
                {{ prosek }}
                <textarea class="type" v-model="comacc">Enter you comment on this account
                </textarea>
                <select v-model="rate">
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                    <option value="6">6</option>
                    <option value="7">7</option>
                    <option value="8">8</option>
                    <option value="9">9</option>
                    <option value="10">10</option>
                </select>
                <div class="ybn" @click="pisi()">Submit Comment</div>
                </div>
            </div>
        </div>
    </div>
</template>