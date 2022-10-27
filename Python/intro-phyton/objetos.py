class Usuario :
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def saludo(self): #metodo
        print('Hola mi nombre es: ', self.nombre ,self.apellido)

class Admin(Usuario) :
    def supersaludo(self):
        print('Hola me llamo ', self.nombre, 'y soy administrador.')



usuario = Usuario('juan', 'muñoz')
usuario2 = Usuario('pedro', 'perez')

usuario.saludo()
usuario2.saludo() 
#el usuario2 #Sirve para borrar un objeto o una instancia

admin = Admin('Alan', 'Muñoz')
admin.saludo()
admin.supersaludo()