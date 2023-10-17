function multiplicar3Numeros (x, y, z){
    return x * y * z;
}
console.log(multiplicar3Numeros(2, 3, 4));
//
const mult = multiplicar3Numeros (4, 5, 6)
console.log(`O valor de mult é: ` + mult);
//
function podeDirigir(idade, cnh){
    if(idade >= 18 && cnh == true){
    console.log("Você pode dirigir!")
} else {
    console.log("Você não pode dirigir!")
}
}
console.log(podeDirigir (19, true));
console.log(podeDirigir(22, false))
console.log(podeDirigir(30, true));
console.log(podeDirigir(16));