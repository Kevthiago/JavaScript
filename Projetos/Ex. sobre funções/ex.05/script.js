let idade = prompt("Digite aqui a sua idade:")
function permission (idade){
    if (idade >= 18){
        console.log("Permissão para a entrada na Auto Escola concedida!");
    } else {
        console.log("Permissão para a entrada na Auto Escola negada!");
    }
}
permission(idade);