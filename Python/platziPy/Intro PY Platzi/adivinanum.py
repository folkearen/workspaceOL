import random 

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Elige un número del 1 al 100: "))

    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Búsca un número mayor")
        else:
            print("Búsca un número menor")
        
        numero_elegido = int(input("Ingresa otro número: "))
        
    print("¡Ganaste!")


if __name__ == "__main__":
    run()