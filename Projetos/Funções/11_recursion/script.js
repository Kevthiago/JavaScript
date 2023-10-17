function recursion(n){
    if (n - 1 < 2){
        console.log("Recursion parou.");
    } else if (n % 2 != 0){
        console.log(`O ${n} é ímpar.`);
        recursion ( n - 1);
    } else {
        console.log(`O ${n} é par.`);
        recursion ( n - 2);
    }
}
recursion(100);
recursion(49);
recursion(10);
