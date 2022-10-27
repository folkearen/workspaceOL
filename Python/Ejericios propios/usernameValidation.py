def valid_username(username):
    if len(username) < 3 or len(username)>10:
        print("Invalid user")
    else: 
        print("Valid user")
    return username

def get_usernae():
    username = input("ingrese nombre: ")
    return username

valid_username(get_usernae())