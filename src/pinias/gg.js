import { defineStore } from "pinia";

export  const userreal = defineStore('userinfo',() => {
    function gg(){
    const tryd = JSON.parse(localStorage.getItem("user"));
    if(tryd){
        console.log("Sigma")
        return tryd;
    }else{
        return false;
    }
}
return {gg}
})
