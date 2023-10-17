const cachorro = {
    raça: "Sem raça definida.",
    uivar: function(){
        console.log("AUUUUUUUUU!");
    },
    rosnar: function(){
        console.log("GRRRRRRRRR!");
    },
    setRaça: function(raça){
        this.raça = raça;
    },
    getRaça: function(){
        return "A raça do cachorro é: " + this.raça;
    }
}
console.log(cachorro.raça);

cachorro.setRaça("Pinscher.");

console.log(cachorro.raça);

console.log(cachorro.getRaça());
 