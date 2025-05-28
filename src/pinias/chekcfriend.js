import { defineStore } from "pinia";
import axios from "axios";
import {ref} from "vue";
export const checkFriend = defineStore('checkFriend',() => {
   
  async  function checkg (user1,user2){
       
     
 const gg =   await axios.get(`http://localhost:8000/api/check/?user1=${user1}&user2=${user2}`).then(res => {
            if(res.data.message >0){
                return true;
            }else{
                return false;
            }
        }).catch(err => console.log(err))
   return  gg;
    };
    return {checkg};
});