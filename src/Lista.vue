<script setup>

import {useRouter} from "vue-router";
import axios from "axios";
import {ref,watch,reactive,computed} from "vue";
import { addFrined } from "./pinias/addFriend";
import { removefriend } from "./pinias/removefriend";
const rev = removefriend();
const gg = addFrined();
const router = useRouter();
const korinsik = computed(() => {
    return localStorage.getItem("user")!=''?JSON.parse(localStorage.getItem("user")) : null;
})
console.log(korinsik.value)
if(!localStorage.getItem("user")){
    router.push('/register/1/')
}
const paralel = ref([]);
const podaci = ref(null)
const search = ref('');
const prijatelji = ref(null)

watch(search, async () => {
    const radi = ref(null)
    if(search.value!=""){
  await axios.get(`http://localhost:8000/api/prijatelj/?ime=${search.value}`).then(res => {podaci.value = res.data.message,radi.value=res.data.message}).catch(err => console.log("Neka Greska"));
 await  axios.get(`http://localhost:8000/api/prijateljd/?user=${JSON.parse(localStorage.getItem("user")).name}`).then(res => prijatelji.value = res.data.message).catch(err => console.log(err))

   paralel.value = await radi.value.map(elem => [elem,false])
for(var i=0;i<paralel.value.length;i++){
    for(var j =0;j<prijatelji.value.length;j++){
        if(paralel.value[i][0].name == prijatelji.value[j].name){
           
            paralel.value[i][1] = true;
            break;
        }
        else{
            continue;
        }
    }
}


    }

})

/*watch(prijatelji.value,() => {
  podaci.value.forEach(element => {
    
  });
})*/
 function addFriendg(user2){
     axios.get(`http://localhost:8000/api/add/?user1=${JSON.parse(localStorage.getItem("user")).name}&user2=${user2}`).then(res => {return res}).catch(err => console.log(err));
console.log("Sad ste prijatelji");
search.value+=" ";
setTimeout(function(){
    search.value = search.value.slice(0,-1)
},10)
}
function removeS(koje){
    rev.remove(korinsik.value.name,koje);
    search.value+=" "
    setTimeout(function(){
    search.value = search.value.slice(0,-1)
},10)
}
function hejbre(user1,user2){
    gg.addFriendG(user1,user2);
     search.value+=" "
    setTimeout(function(){
    search.value = search.value.slice(0,-1)
},10)
}
</script>
<template>
    <div class="users">
        
        <input type="text" class="search" v-model="search">
       
        <div class="list">
            <img>
        
            <div class="prijatelji" v-for="(jojs,index) in paralel" :key="index">
                
                    <div class="add" @click="hejbre(korinsik.name,jojs[0].name)"  v-if="!paralel[index][1]">Add Friend</div>
                    <div v-else class="add r" @click="removeS(jojs[0].name)">Vec Ste prijatelji</div>
                <div class="jname">Ime:{{ jojs[0].name }}</div>
                <div class="jgmail">gmail:{{ jojs[0].name }}</div>
                <div class="ver">
          
                 <img width="30px" height="30px" src="./assets/upitnik-removebg-preview.png" v-if="!jojs.verif">
                 <img v-else width="30px" height="30px" src="./lol.png">
                </div>
            </div>
            <div class="podaci" v-if="!podaci">
                Loading
                <div class="dots">
                    <div class="dot"></div>
                    <div class="dot"></div>
                    <div class="dot"></div>
                </div>
            </div>
        </div>
    </div>
</template>