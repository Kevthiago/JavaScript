let nome = "Kevin";
let nome2 = "Thiago";
let test = nome = nome2 = prompt("Qual é o seu nome?");

switch(test){
    case "Kevin":
        console.log("O nome é Kevin.");
        break;
    case "Thiago":
        console.log("O nome é Thiago.");
        break;
    default:
        console.log("O nome não foi encontrado.");
        break;
}

/*if (nome == "kévin"){
   console.log("O nome é Kevin.")
  } else {
    console.log("O nome não foi encontrado.")
  }
*/