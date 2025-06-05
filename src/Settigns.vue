<script setup>
    import {onMounted, ref, watch} from "vue";
    import { defineEmits } from "vue";
    import animback from "./animationblocks/animback.vue";
    import axios from "axios";
    import {userreal} from "./pinias/gg"
import { walk } from "vue/compiler-sfc";
    const userg = userreal();
    const kori =userg.gg();
    const si  = ref(false);
    const vre = ref("Hello your histroy wait for you")
    const emits = defineEmits(["closed"],["openg"])
    const props = defineProps({
        klik:Boolean
    })
    const joj = props.klik;
    function cls(){
        emits("closed",false)
    }
    const hover = ref(false);
    function isH(){
        if(props.klik=true){
            cls()
        }else{

        }
    }
    function hopen(){
        emits("openg","kj")
    }
    const texta = ref("");
    const fj = ref(false);
    const prikzi = ref(false)
    function updateh(){
        prikzi.value = true;
        if(kori){
          console.log(kori.id)
        axios.get(`http://localhost:8000/api/anout/?id=${kori.id}&data=${texta.value}`).then(res => prikzi.value=false).catch(err => console.log(err))
        }
    }
    onMounted( () => {
        console.log("asdasdasdasdasdasd")
         axios.get(`http://localhost:8000/api/getabout/?name=${kori.id}`).then(res => {texta.value = res.data.message[0].about;console.log(vre.value)}).catch(err => console.log(err));
    })

   
</script>
<template>
      <div class="options" :class={opj:props.klik}>
        <div class="rel">
            <div class="back" @click="isH()">
                <img src="./curve-arrow-pointing-left.png" width="30px" height="30px">
            </div>
            <div class="menu">
               
                    
                <div class="option">
                    <div class="rel" @mouseenter="hover=true" @mouseleave="hover=false">
                        
                    ?<animback gg="20" :hv="hover"></animback></div>
                </div>
            </div>
            <div class="tings">
                <div class="rel">
                    <div class="thg1">
                        <div class="rel">
                            <div class="cell" style="margin-top: 30%;">
                                <h3 class="cell">See your data</h3>
                                <p class="cell">See all of your data which was saved on your localStorage cliking on this button below this text,if you have any errors or problems please contact our support team.</p>
                                <button class="nbtn" @click="hopen()">Get Data</button>
                                <div class="cell">
                                <h3 class="cell">Verify your Gmail</h3>
                                <p class="cell">Here you can clicking on link below go and verify you gmail adress who you entered when you regsitered;this will take maybe several minuts in case how much server is active.</p>
                           <router-link to="/gmail/"><button class="nbtn">Verify Gmail</button></router-link>
                          
                           <div class="cell">
                            <h3 class="cell">Get full verifited by choosing one of following plans</h3>
                            <p class="cell">When you buy one of these plans you will forever get veryfied badge but only if you frequently every year submit your mobile phone,for more info click on phots and learn more about it.</p>
                           </div>
                     
                           <div class="cell">
                        <h3 class="cell">
                            Tell us more about your self
                        </h3>
                        <p class="cell">
                            Type somethng that can will most likly represent you for someone when thay reads that here.

                        </p>
                        <div class="cell start">
                       
                        <textarea name="" id="" v-model="texta">
                           
                           
                        </textarea>
                  
                        <button @click="updateh()">Update Data</button>
                        <div v-if="prikzi">
                        Loading
                        </div>
                        </div>
                           </div>
                           <br><br><br><br><br>
                           <div class="cell">
                            <div class="out">Sign out</div>

                           </div>
                           
                         
                           
                           
                            </div>
                            </div>
                         
                        </div>
                    </div>
                </div>
            </div>
            <div></div>
        </div>
      </div>
</template>