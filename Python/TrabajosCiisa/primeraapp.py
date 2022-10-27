from tkinter import *
from PIL import ImageTk, Image

ventana = Tk()
ventana.title("Mis imagenes")
ventana.geometry("600x350")

imagen1 = ImageTk.PhotoImage(Image.open("C:/Users/alanm/Escritorio/fotos/f1.jfif"))
imagen2 = ImageTk.PhotoImage(Image.open("C:/Users/alanm/Escritorio/fotos/f2.jfif"))
imagen3 = ImageTk.PhotoImage(Image.open("C:/Users/alanm/Escritorio/fotos/f3.jfif"))

lista = [imagen1, imagen2, imagen3]

label = Label(ventana, image = imagen1)

label.grid(row=0, column=0, columnspan=3)


def adelante(image_number):
    global label
    global adelante_boton
    global atras_boton
    label.grid_forget()
    label = Label(image = lista[image_number -1])
    adelante_boton = Button(ventana, text="Adelante", width= 20, command=lambda:adelante(image_number +1))
    atras_boton = Button(ventana, text="Atrás", width= 20, command=lambda: atras(image_number -1))

    if image_number == 3:
        adelante_boton = Button(ventana, text="Adelante", width= 20, state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    atras_boton.grid(row=1, column=0)
    adelante_boton.grid(row=1, column=2)

def atras(image_number):
    global label
    global adelante_boton
    global atras_boton
    label.grid_forget()
    label = Label(image = lista[image_number -1])
    adelante_boton = Button(ventana, text="Adelante", width= 20, command=lambda:adelante(image_number +1))
    atras_boton = Button(ventana, text="Atrás", width= 20, command=lambda: atras(image_number -1))

    if image_number == 1:
        atras_boton = Button(ventana, text="Atras", width= 20, state=DISABLED)
    label.grid(row=0, column=0, columnspan=3)
    atras_boton.grid(row=1, column=0)
    adelante_boton.grid(row=1, column=2)

atras_boton = Button(ventana, text="Atrás", width= 20, command=DISABLED)
salir_boton = Button(ventana, text="Salir", width= 20, command=ventana.quit)
adelante_boton = Button(ventana, text="Adelante", width= 20, command=lambda:adelante(2))

atras_boton.grid(row=1, column=0)
salir_boton.grid(row=1, column=1)
adelante_boton.grid(row=1, column=2)

ventana.mainloop()