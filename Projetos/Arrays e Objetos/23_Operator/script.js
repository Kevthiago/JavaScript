let a = 1;
let b = 2;
let c = 3;
let d = 4;
let e = 5;

function imprimirNumeros (...args) {
    for(let i = 0; i < args.length; i = i + 1) {
        console.log(args[i]);
    }
}

imprimirNumeros (a, b, c, d, e);
imprimirNumeros (b, c, d, e);
