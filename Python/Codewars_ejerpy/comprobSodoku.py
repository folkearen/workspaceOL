"""
fondo de sudoku
Sudoku es un juego que se juega en una cuadrícula de 9x9. El objetivo del juego es llenar todas las celdas de la cuadrícula con dígitos del 1 al 9, de modo que cada columna, cada fila y cada una de las nueve subcuadrículas de 3x3 (también conocidas como bloques) contengan todos los dígitos del 1 a 9.
(Más información en: http://en.wikipedia.org/wiki/Sudoku )

Validador de soluciones de Sudoku
Escriba una función validSolution// que acepte una matriz 2D que represente un tablero de Sudoku ValidateSolutiony valid_solution()devuelva verdadero si es una solución válida, o falso en caso contrario. Las celdas del tablero de sudoku también pueden contener 0, que representarán celdas vacías. Los tableros que contienen uno o más ceros se consideran soluciones no válidas.

El tablero siempre tiene 9 celdas por 9 celdas, y cada celda solo contiene números enteros del 0 al 9.

validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]); // => true

validSolution([
  [5, 3, 4, 6, 7, 8, 9, 1, 2], 
  [6, 7, 2, 1, 9, 0, 3, 4, 8],
  [1, 0, 0, 3, 4, 2, 5, 6, 0],
  [8, 5, 9, 7, 6, 1, 0, 2, 0],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 0, 1, 5, 3, 7, 2, 1, 4],
  [2, 8, 7, 4, 1, 9, 7, 3, 5],
  [3, 0, 0, 4, 8, 1, 1, 7, 9]
]); // => false
"""

#Creo que hay que corregir y supervisar las prociones de 3 X 3

def validSolution (matriz):
  matrizAlterna = [[],[],[],[],[],[],[],[],[]]
  contador = 0
  for i in matrizAlterna:
      for j in range(0,9):
          i.append(matriz[j][contador])
      if 0 in matrizAlterna[contador]:
          return False
      contador += 1
      comprobacion = [1,2,3,4,5,6,7,8,9]
  for j, i in zip(matriz, matrizAlterna):
    if sorted(j) != comprobacion or sorted(i) != comprobacion:
      return False
  return True
      
print(validSolution ([ 
  [1, 2, 3, 4, 5, 6, 7, 8, 9]
 ,[2, 3, 4, 5, 6, 7, 8, 9, 1]
 ,[3, 4, 5, 6, 7, 8, 9, 1, 2]
 ,[4, 5, 6, 7, 8, 9, 1, 2, 3]
 ,[5, 6, 7, 8, 9, 1, 2, 3, 4]
 ,[6, 7, 8, 9, 1, 2, 3, 4, 5]
 ,[7, 8, 9, 1, 2, 3, 4, 5, 6]
 ,[8, 9, 1, 2, 3, 4, 5, 6, 7]
 ,[9, 1, 2, 3, 4, 5, 6, 7, 8]])) # Da True y debe ser false
