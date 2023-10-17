function imprimirNumeros(num) {
    for(let x = num; x >= 0; x--){
        if(x % 2 == 0){
            console.log(`O número ${x} é par.`)
        }
    }
}
console.log(imprimirNumeros(100));
