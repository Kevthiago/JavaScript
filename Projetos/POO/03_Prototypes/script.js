const humano = {
    mãos: 2,
}
console.log(Object.getPrototypeOf(humano));
console.log(Object.getPrototypeOf(humano) === Object.prototype);

console.log(humano.hasOwnProperty("mãos"));