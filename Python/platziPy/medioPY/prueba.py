def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    numero = input("Ingresa un numero ")
    try:
        numero = int(numero)
    except:
        assert numero.isnumeric(), "Debe ingresar numeros no letras"
    try:
        if numero < 0:
            raise ValueError ("Debes ingresar numeros positivos")
        print(divisors(numero))
    except ValueError as ve:
        print(ve)
        return False



if __name__ == '__main__':
    run()
