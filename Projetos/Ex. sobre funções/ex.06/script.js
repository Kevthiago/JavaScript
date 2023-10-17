function detect (dado){
    if (typeof dado === 'number'){
        console.log("Este dado é um Number");
    } else if (typeof dado === 'string'){
        console.log("Este dado é uma String");
    } else if ( typeof dado === 'boolean'){
        console.log("Este dado é um Boolean");
    }
}
detect("Oi");
detect(20);
detect("Kevin" != "Poly");
