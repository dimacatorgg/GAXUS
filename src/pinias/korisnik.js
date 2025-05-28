import { defineStore } from "pinia";

export const userreal = defineStore('userinfo',() => {
    function korinsik(){
    const tryd = JSON.parse(localStorage.getItem("user"));
    if(tryd){
        return tryd;
    }else{
        return false;
    }
}
return {korinsik}
})