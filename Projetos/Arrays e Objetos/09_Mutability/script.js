let carroA = {
    "Marca" : "Volkswagem",
};

carroB = carroA;

let carroC = {
    "Marca" : "Volksvagem"
};

console.log(carroA == carroB);
console.log(carroA == carroC);

console.log(carroA.Marca);
console.log(carroB.Marca);
console.log(carroC.Marca);
