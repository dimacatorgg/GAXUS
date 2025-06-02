
<script setup>
import {onMounted, ref, watch,computed} from "vue";
const porps = defineProps({
    gg:String,
    hv:Boolean
})
const huj = ref([]);
for(var i=0;i<Number(porps.gg);i++){
    huj.value.push([''])
}

const ins = ref(null);
onMounted(() => {
    for(var i=0;i<ins.value.length;i++){
        ins.value[i].style.width = Math.floor(ins.value[i].parentElement.offsetWidth/3) -1 + "px";
        ins.value[i].style.height = ins.value[i].parentElement.offsetHeight/Number(porps.gg) + 10 + "px";
        ins.value[i].style.transition = "all " + (porps.gg/5)/i +"s";
     
    }

})
const isHover = computed(() =>  porps.hv)
watch(isHover,() => {

    if(isHover.value==true){
        for(var i=0;i<ins.value.length;i++){
        ins.value[i].classList.add("red")
      
     
    }
    }else{
        for(var i=0;i<ins.value.length;i++){
        ins.value[i].classList.remove("red")
      
     
    }
    }
})
</script>




<template>

<div class="animgo">
    <div class="rel">
    <div class="blocksd" v-for="hj,index in huj" ref="ins" :key="index">
       
    </div>
    </div>
</div>


</template>