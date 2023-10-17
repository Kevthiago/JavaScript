let carro = {
    marca: 'Honda',
    modelo: "HR-V",
    ano: 2023,
    dono: "Kévin",
}
console.log(carro.marca);
console.log(carro.modelo);
console.log(carro.ano);
console.log(carro.dono);

delete carro.ano;
delete carro.dono;

console.log(carro.marca);
console.log(carro.modelo);
console.log(carro.ano);
console.log(carro.dono);
