from cgitb import text
from pprint import pprint
from textwrap import fill
import tkinter
import pprint

window = tkinter.Tk()

label_saludo = tkinter.Label(window, text="Hola mundo", bg="cyan", fg="blue")
label_saludo.pack(ipadx=50, ipady=50, fill="both")

label_adios = tkinter.Label(window, text="Adios mundo", bg="black", fg="white")
label_adios.pack(ipadx=100, ipady=100, fill="both")



window.mainloop()
