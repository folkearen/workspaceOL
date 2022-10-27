def divisors(num):
    divisor = []
    for i in range (1,num + 1):
        if num % i == 0:
            divisor.append(i)
    return divisor

def run():
    numero = int(input("Ingresa un numero "))
    try:
        if numero < 0:
            raise ValueError ("Debes ingresar numeros positivos")
        print(divisors(numero))
    except ValueError as ve:
        print(ve)
        return False



if __name__ == '__main__':
    run()