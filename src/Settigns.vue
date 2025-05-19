<script setup>
    import {ref} from "vue";
    const si  = ref(false);
    const props = defineProps({
        klik:Boolean
    })
    const joj = props.klik;

</script>
<template>
       <div class="options" :class="{opl : joj}">
            <div class="rel">
            <div class="leftclose" @click="joj = !joj">
                <img src="./curve-arrow-pointing-left.png" width="40px" height="40px">
            </div>
            </div>
        </div>
        <div class=""></div>
</template>