let pessoa = {
    nome: "Kévin",
    idade: 20,
    profissão: "Cientista da Computação",
    hobby: ["Valorant", "GYM", "Futsal"]
}

let pessoaTexto = JSON.stringify(pessoa);
console.log(pessoaTexto);

//

let pessoaJSON = JSON.parse(pessoaTexto);
console.log(pessoaJSON);