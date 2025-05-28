import { defineStore } from "pinia";
import axios from "axios";
export const removefriend = defineStore("removeFriend",() => {
    function remove(user1,user2){
        axios.get(`http://localhost:8000/api/del/?user1=${user1}&user2=${user2}`).then(res => console.log("Sve je okje odradjeno")).catch(err => console.log(err))
        console.log("Hej")
    }
    return {remove}
})