function random(q){
    return Math.floor(Math.random()*q);
}
export default random;
class Human{
    constructor(name,age){
        this.name=name;
        this.age = age
    }
    prica(nes){
        console.log(nes + "Covek k oji ima" + this.age)
    }
}
var hej = new Human("Dimtirije",16)
hej.prica("Ja sam " + hej.name)