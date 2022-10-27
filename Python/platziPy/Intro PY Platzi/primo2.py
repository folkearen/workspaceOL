def run():
    numero = int(input('Ingresa un numero: '))
  
    if numero == 1:
            print('0 y 1 no se consideran primos') 

    elif numero != 1:
        for i in range(2, numero): #En caso de ser el numero un 2
            #el for no se ejecuta porque el range no puede ir de un 
            #numero mayor a uno menor simplemente, o sea de 2 a1
            if  numero % i == 0:
                print('Este numero no es primo')
                break      
        else:
            print('Este numero es primo')

       
if __name__=='__main__':
    run()