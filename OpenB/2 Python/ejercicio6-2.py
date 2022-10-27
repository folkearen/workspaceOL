class Alumno:
    nombre = ""
    nota = 0

    def ingresarNombre(self):
        nombre=input("Ingrese nombre: ")
        self.nombre = nombre
    
    def ingresarNota(self):
        nota= float(input("Ingrese nota, con máximo un decimal: "))
        self.nota = nota

    def imprimirDatos(self):
        print("Nombre del estudiante: ", self.nombre)
        print("Nota del estudiante: ", self.nota)
    
    def comprobarAprobacion(self):
        if self.nota > 3.9:
            print("Aprobado")
        else:
            print("Desaprobado")
def run(id = input("Ingrese ID: ")):
    globals()[id] = Alumno()
    globals()[id].ingresarNombre()
    globals()[id].ingresarNota()
    globals()[id].imprimirDatos()
    globals()[id].comprobarAprobacion()

 

if __name__ == '__main__':
    run()
    