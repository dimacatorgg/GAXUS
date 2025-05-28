<script setup>
import {ref,computed} from "vue";
import axios from "axios";
const ert = ref("")
const ins = ref(null);
function submit(){
    if(!ins.value){
        ert.value = "Errror"
    }else{
        axios.get(`http://localhost:8000/api/ntest/?name=${ins.value}`).then(res => console.log(res)).catch(err => console.log(err))
    }
}
</script>
<template>
    <input v-model="ins">
    <button @click="submit">Submit</button>
    {{ ert }}
</template>