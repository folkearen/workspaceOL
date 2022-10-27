"""Diccionarios que contien listas y listas que contiene diccinarios"""

def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {'Firstname': 'Alan', 'Lastname': 'Munoz'}


    # Lista de diccionarios
    super_list = [
        {'Firstname': 'Alan', 'Lastname': 'Munoz'},
        {'Firstname': 'Tamara', 'Lastname': 'Badillo'},
        {'Firstname': 'Maria', 'Lastname': 'Guerra'},
        {'Firstname': 'Julio', 'Lastname': 'Cifuentes'},
        {'Firstname': 'Pascal', 'Lastname': 'Troncoso'},
    ]
    

    # Diccionario de listas
    super_dict = {
        'naturals_nums':[1, 2, 3, 4, 5],
        'integer_nums': [-1, -2, 0, 1, 2],
        'float_nums': [1.1, 4.5, 6.43]
    }
  
    for key, value in super_dict.items():
        print(f'{key} - {value}')

    for i in super_list:
        print(i)
        
    for i in super_list:
        for key, value in i.items():
            print(f'{key}-{value}')
    
    for i in super_list:
        print(i.items())
    
    for item in super_list:
        print(item["Firstname"] , "-" , item["Lastname"])

if __name__=='__main__':
    run()