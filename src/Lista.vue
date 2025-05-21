<script setup>

import {useRouter} from "vue-router";
import axios from "axios";
import {ref,watch,reactive} from "vue"
const router = useRouter();

if(!localStorage.getItem("user")){
    router.push('/register/1/')
}
const podaci = ref(null)
const search = ref('');
const prijatelji = ref(null)
watch(search, () => {
   axios.get(`http://localhost:8000/api/prijatelj/?ime=${search.value}`).then(res => {podaci.value = res.data.message}).catch(err => console.log("Neka Greska"))
    axios.get(`http://localhost:8000/api/prijateljd/?user=${JSON.parse(localStorage.getItem("user")).name}`).then(res => prijatelji.value = res.data.message).catch(err => console.log(err))

})
/*watch(prijatelji.value,() => {
  podaci.value.forEach(element => {
    
  });
})*/
 function addFriend(user2){
     axios.get(`http://localhost:8000/api/add/?user1=${JSON.parse(localStorage.getItem("user")).name}&user2=${user2}`).then(res => {return res}).catch(err => console.log(err));
console.log("Sad ste prijatelji")

}
</script>
<template>
    <div class="users">
        <input type="text" class="search" v-model="search">
        <div class="list">
            <img>
            <div class="prijatelji" v-for="jojs in podaci">
                
                    <div class="add" @click="addFriend(jojs.name)">Add Friend</div>
                <div class="jname">Ime:{{ jojs.name }}</div>
                <div class="jgmail">gmail:{{ jojs.gmail }}</div>
                <div class="ver">
          
                 <img width="30px" height="30px" src="./assets/upitnik-removebg-preview.png" v-if="!jojs.verif">
                 <img v-else width="30px" height="30px" src="./lol.png">
                </div>
            </div>
            <div v-if="!podaci">Lodaing</div>
        </div>
    </div>
</template>