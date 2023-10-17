function lembrarSoma(x){
    return function(y){
        return x + y;
    }
}
let soma1 = lembrarSoma(10);
console.log(soma1(3));
let soma2 = lembrarSoma(8);
console.log(soma2(3));
//
function contador (i){
    let cont = i;
    let somarContador = function(){
        console.log(cont)
        cont++;
    }
    return somarContador
}
let meucontador = contador(5);
meucontador();
meucontador();
meucontador();
meucontador();
meucontador();
meucontador();
meucontador();