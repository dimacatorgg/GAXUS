<script setup>
import animback from './animationblocks/animback.vue';
import {ref,computed} from "vue"
import { userreal } from './pinias/gg';
import { defineEmits } from 'vue';
import { Transition } from 'vue';
const props = defineProps({
    otvoreno:Boolean
})
const emit = defineEmits(["otvoreno"]);
function zatvori(){
    emit("otvoreno","hej")
}
const g = userreal();
const h = g.gg();
</script>


<template>


<transition>
    <div class="infog" v-if="props.otvoreno">
        <div class="rel">
            <div class="headerg">
                Following data is represented in JSON format
            </div>
            <div class="bodyg">
                <div class="kext">
                    The following data that you would find in table below this text conatins all info that were stored in your PC only in way to improve user expirince,in strict way to avoid constant fething data.
                </div>
                <div class="cen" style="justify-content: center;">
                <div class="table">
                    <div class="tableg-r">
                        <div class="elemg">Username</div>
                        <div class="elemg">userid</div>
                        <div class="elemg">gmail</div>
                    </div>
                    <div class="tableg-w">
                        <div class="elemg">{{ h.name }}</div>
                        <div class="elemg">{{ h.gmail }}</div>
                        <div class="elemg">{{ h.id }}</div>
                    </div>
                </div>
                </div>
                <div class="cen">
                <button class="cbtn green">
                   
                    Get Data in JSON</button>
                <button class="cbtn" @click="zatvori">Close</button>
                </div>
            </div>
        </div>
    </div>

</transition>

</template>
<style>
    .v-enter-active, .v-leave-active {
  transition: opacity 0.5s;
}
.v-enter-from,.v-enter, .v-leave-to {
  opacity: 0;
}

</style>