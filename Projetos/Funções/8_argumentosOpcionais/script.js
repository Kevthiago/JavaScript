function soma (a, b) {
    if (a === undefined || b === undefined){
        console.log('Esta função precisa ter os dois argumentos!')
    } else {
        return a + b;
    }
}
console.log(soma(1));
console.log(soma(3,3));
//
function saudacao(nome, idade){
    if (idade === undefined){
        console.log("Saudações " + nome, "!")
    } else{
        console.log("Saudações," + nome, "! Você tem " + idade, "anos.")
    }
}
console.log(saudacao("Kévin", 20));
console.log(saudacao("Poly"));