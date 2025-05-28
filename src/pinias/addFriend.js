import { defineStore } from "pinia";
import axios from "axios";
export const addFrined = defineStore('addFriend',() => {
    function addFriendG(user1,user2){
       
        axios.get(`http://localhost:8000/api/add/?user1=${user1}&user2=${user2}`).then(res => {return res}).catch(err => console.log(err));
        console.log("Sad ste prijatelji");
      
       
    }
    return {addFriendG}
})