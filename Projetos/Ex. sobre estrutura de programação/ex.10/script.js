let x = prompt("Digite um número:")
let div = 0;
for(i = 1; i <= x; i++){
    if(x % i == 0){
        div++;
    }
}

if( div == 2){
    console.log(`O número ${x} é primo.`)
} else{
    console.log(`O número ${x} não é primo.`)
}