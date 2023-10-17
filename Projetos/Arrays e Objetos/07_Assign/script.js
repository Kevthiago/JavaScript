let carro = {
    portas: 4,
    motor: 2.0,
    portamalas: "200 litros",
}

let adicionais = {
    arCondicionado: true,
    tetoSolar: true,
}

console.log(carro);

Object.assign(carro, adicionais);

console.log(carro);
