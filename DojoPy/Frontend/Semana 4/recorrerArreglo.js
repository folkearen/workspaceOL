let nombres = ["Alan", "Maria", "Julio"]

nombres.forEach(function(nom,i,arreglo){
    console.log(`${i} ${nom} ${arreglo}`)
})

let numeros = [100,200,300,400]

let cuenta = numeros.map((monto,indice,array)=>{
    return `Cuenta ${indice} - ${monto + 120}`
})

