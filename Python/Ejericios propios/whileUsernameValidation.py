def valid_username(username):
    if len(username) > 3 and len(username)<10:
        return username

def get_username():
    username = input("ingrese nombre: ")
    return username

username = get_username()

while not valid_username(username):
    print("Invalid username")
    username = get_username()

print("Valid user")