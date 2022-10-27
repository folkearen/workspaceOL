let peliculas = [
    {nombrePelicula: "Sucker Punch",
     annio: 2011,
     director: "Zack Snyder",
     genero: "Ciencia Ficcion" }, 

     {nombrePelicula: "Angle-A",
     annio: 2005,
     director: "Luc Besson",
     genero: "Comedia Romantica"},

     {nombrePelicula: "El contador",
     annio: 2016,
     director: "Gavin O`Connor",
     genero: "Accion"}

]



for(let i=0; i<peliculas.length; i++){
    console.log(`La pelicula ${peliculas[i].nombrePelicula}, se estrno en el 
    año ${peliculas[i].annio}, su director es ${peliculas[i].director} y
    pertenece al genero de ${peliculas[i].genero}`)
}