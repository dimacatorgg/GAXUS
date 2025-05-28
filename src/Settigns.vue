<script setup>
    import {ref} from "vue";
    import { defineEmits } from "vue";
    import animback from "./animationblocks/animback.vue";
    const si  = ref(false);
    const emits = defineEmits(["closed"])
    const props = defineProps({
        klik:Boolean
    })
    const joj = props.klik;
    function cls(){
        emits("closed",!props.klik)
    }
    const hover = ref(false);
</script>
<template>
      <div class="options" :class={opj:props.klik}>
        <div class="rel">
            <div class="back" @click="cls()">
                <img src="./curve-arrow-pointing-left.png" width="30px" height="30px">
            </div>
            <div class="menu">
               
                    
                <div class="option">
                    <div class="rel" @mouseenter="hover=true" @mouseleave="hover=false">
                        
                    ?<animback gg="10" :hv="hover"></animback></div>
                </div>
            </div>
            <div></div>
        </div>
      </div>
</template>