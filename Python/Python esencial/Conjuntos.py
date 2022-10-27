"""Para crear un conjunto especificamos sus elementos entre llaves:"""

a = {1,2,3}
print(type(a))

"""Al igual que otras colecciones, sus miembros pueden ser de diversos tipos:"""

s = {True, 3.14, None, False, "Hola mundo", (1, 2)}

"""No obstante, un conjunto no puede incluir objetos mutables como listas, diccionarios, e incluso otros conjuntos."""

"""Python distingue este tipo operación de la creación de un diccionario ya que no incluye dos puntos. Sin embargo, no puede dirimir el siguiente caso y por defecto crea un diccionario:"""

s = {}

""" Para generar un conjunto vacío, directamente creamos una instancia de la clase set:"""

s = set()

"""De la misma forma podemos obtener un conjunto a partir de cualquier objeto iterable:"""
s1 = set([1, 2, 3, 4])
s2 = set(range(10))

"""Un set puede ser convertido a una lista y viceversa. En este último caso, los elementos duplicados son unificados."""

list({1, 2, 3, 4})
# Arroja [1, 2, 3, 4]

set([1, 2, 2, 3, 4])
# Arroja {1, 2, 3, 4}

"""Los conjuntos son objetos mutables. Vía los métodos add() y discard() podemos añadir y remover un elemento indicándolo como argumento."""

s = {1, 2, 3, 4}
s.add(5)
s.discard(2)
# Arrojas{1, 3, 4, 5}

"""Nótese que si el elemento pasado como argumento a discard() no está dentro del conjunto es simplemente ignorado. En cambio, el método remove() opera de forma similar pero en dicho caso lanza la excepción KeyError.

Para determinar si un elemento pertenece a un conjunto, utilizamos la palabra reservada in."""

"""La función clear() elimina todos los elementos."""

s = {1, 2, 3, 4}
s.clear()

"""El método pop() retorna un elemento en forma aleatoria (no podría ser de otra manera ya que los elementos no están ordenados). Así, el siguiente bucle imprime y remueve uno por uno los miembros de un conjunto."""

while s:
    print(s.pop())

"""remove() y pop() lanzan la excepción KeyError cuando un elemento no se encuentra en el conjunto o bien éste está vacío, respectivamente."""

"""Para obtener el número de elementos aplicamos la ya conocida función len():"""

len({1, 2, 3, 4})

"""Operaciones principales
Algunas de las propiedades más interesantes de los conjuntos radican en sus operaciones principales: unión, intersección y diferencia.

La unión se realiza con el caracter | y retorna un conjunto que contiene los elementos que se encuentran en al menos uno de los dos conjuntos involucrados en la operación."""

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a | b
#  Resultado {1, 2, 3, 4, 5, 6} omite los elementos que s eencuentran en ambos

"""La intersección opera de forma análoga, pero con el operador &, y retorna un nuevo conjunto con los elementos que se encuentran en ambos."""

a & b
# Arroja{3, 4} Solo crea el conjunto con los elementos que se repiten en ambos

"""La diferencia, por último, retorna un nuevo conjunto que contiene los elementos de a que no están en b."""

a = {1, 2, 3, 4}
b = {2, 3}
a - b
# Arroja {# Arroja 1, 4}

"""Dos conjuntos son iguales si y solo si contienen los mismos elementos (a esto se lo conoce como principio de extensionalidad):"""

{1, 2, 3} == {3, 2, 1}
# Arroja True
{1, 2, 3} == {4, 5, 6}
# Arroja False

"""Otras operaciones
Se dice que B es un subconjunto de A cuando todos los elementos de aquél pertenecen también a éste. Python puede determinar esta relación vía el método issubset()."""

a = {1, 2, 3, 4}
b = {2, 3}
b.issubset(a)
# Arroja True

"""Inversamente, se dice que A es un superconjunto de B."""
a.issuperset(b)
# Arroja  True

"""La definición de estas dos relaciones nos lleva a concluir que todo conjunto es al mismo tiempo un subconjunto y un superconjunto de sí mismo."""

a = {1, 2, 3, 4}
a.issubset(a)
#  Arroja True
a.issuperset(a)
# Arroja True

"""La diferencia simétrica retorna un nuevo conjunto el cual contiene los elementos que pertenecen a alguno de los dos conjuntos que participan en la operación pero no a ambos. Podría entenderse como una unión exclusiva."""

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a.symmetric_difference(b)
# Arrpja {1, 2, 5, 6} retonarla los elemntos no repetidos entre los conjuntos

"""Por último, se dice que un conjunto es disconexo respecto de otro si no comparten elementos entre sí."""

a = {1, 2, 3}
b = {3, 4, 5}
c = {5, 6, 7}
a.isdisjoint(b)
# Arroja False  # No son disconexos ya que comparten el elemento 3.
a.isdisjoint(c)
# Arroja True   # Son disconexos.

"""En otras palabras, dos conjuntos son disconexos si su intersección es el conjunto vacío, por lo que puede ilustrarse de la siguiente forma:"""

def isdisjoint(a, b):
    return a & b == set()

isdisjoint(a, b)
# Arroja False
isdisjoint(a, c)
# Arroja True


"""Conjuntos inmutables
frozenset es una implementación similar a set pero inmutable. Es decir, comparte todas las operaciones de conjuntos provistas en este artículo a excepción de aquellas que implican alterar sus elementos (add(), discard(), etc.). La diferencia es análoga a la existente entre una lista y una tupla.
"""
a = frozenset({1, 2, 3})
b = frozenset({3, 4, 5})
a & b
#  Arroja frozenset({3})
a | b
#  Arroja frozenset({1, 2, 3, 4, 5})
a.isdisjoint(b)
#  Arroja False

"""Esto permite, por ejemplo, emplear conjuntos como claves en los diccionarios:"""
a = {1, 2, 3}
b = frozenset(a)
{a: 1}
# Traceback (most recent call last):
#   ...
# TypeError: unhashable type: 'set'
{b: 1}
# Arroja {frozenset({1, 2, 3}): 1}

"""
a|b union, de conjunto a con conjunto b. se omiten los repetidos.
a&b interseccion, que elemntos tengo presente en ambos conjuntos.
a-b diferencia, que elemntos se encuentran solo en el conjunto a.
a^b diferencia simetricaa, que elementos se encuentran solo en uno de los conjuntos, cosiderando ambos conjuntos.
"""