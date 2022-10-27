"""Ejercio 1
La función email_list recibe un diccionario, que contiene nombres de dominio como claves
 y una lista de usuarios como valores. Complete los espacios en blanco para generar una 
 lista que contenga direcciones de correo electrónico completas (por ejemplo, 
 diana.prince@gmail.com).
"""
def email_list(domains):
    emails = [] #Crea la lista vacia.
    for domain, users in domains.items(): #Recorro el diccinario domains, separando la clave
        #que es nomebre de dominio en la variable domain y la lista de usuarios que es ;
        #el valor de la clave en la variable users.
        for user in users: #recorro la lista que son los valores de la clave
            emails.append(user + "@" + domain) #Agrefa los usuarios a la lista y eles va 
            #agregamnndo @ y el dominio almacenado en domain que son las claves del dic.
    return(emails)#Retorna la lista con usuario y respectivo dominio alamacenados en la
    #lista emails, OJO!! habia puesto el return dentro del segundo for, solo retornado
    #los usuarios con el primer dominio @gmail.

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))


"""Ejercicio 2
La función groups_per_user recibe un diccionario, que contiene nombres de grupos con la lista 
de usuarios. Los usuarios pueden pertenecer a varios grupos. Rellene los espacios en blanco 
para devolver un diccionario con los usuarios como claves y una lista de sus grupos como 
valores.
"""

def groups_per_user(group_dictionary):
    user_groups = {} #Diccionario vacio
    for group, users in group_dictionary.items():
        #print(group, users) #local, [admin, userA] cic1 / public, [admin, userB] cic2/administrator, []admin
        for user in users: #admin / userA // admin/userB// admin/usearA
            if user not in user_groups:
                user_groups[user] = [] #admin : [] / userA:[] // userB[]
            user_groups[user].append(group) #admin:[local, public, administrator] / userA[local]//userB[public] 

    return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin", "userA"] }))


"""Ejercicio 3
La función add_prices devuelve el precio total de todos los comestibles en el diccionario.
Rellene los espacios en blanco para completar esta función.
"""
def add_prices(basket):
    total = 0
    for price in basket.values():
        total += price
    return round(total, 2)

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44