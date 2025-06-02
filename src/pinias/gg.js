import { defineStore } from "pinia";

export  const userreal = defineStore('userinfo',() => {
    function korinsikg(){
    const tryd = JSON.parse(localStorage.getItem("user"));
    if(tryd){
        console.log("Sigma")
        return tryd;
    }else{
        return false;
    }
}
return {korinsikg}
})
