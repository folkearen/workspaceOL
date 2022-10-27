"""
La empresa para la que trabaja acaba de adjudicarse un contrato para construir una pasarela de pago. Para ayudar a que las cosas avancen, se ha ofrecido como voluntario para crear una función que tomará un valor flotante y devolverá el formato de la cantidad en dólares y centavos.

39.99 becomes $39.99

El resto de su equipo se asegurará de que el argumento se desinfecte antes de pasarlo a su función, aunque deberá tener en cuenta la adición de ceros finales si faltan (aunque no tendrá que preocuparse por un punto pendiente).

Ejemplos:

3 needs to become $3.00

3.1 needs to become $3.10
"""


def format_money(amount):
    return f'${amount :.2f}'

print(format_money(3.99))