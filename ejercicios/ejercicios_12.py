from tkinter import *

root = Tk()

root.title("cuadro")
#nombre
Label(root, text="Nombre:").grid(row=0, column=0)
nombre = Entry(root)
nombre.grid(row =0, column= 1 )

#edad
Label(root, text="Edad").grid(row=1, column=0)
edad = Entry(root)
edad.grid(row=1, column=1)

def mostrar_boton():
    name = nombre.get()
    age = edad.get()
    Label(root, text=f"tu nombre es {name} y tienes {age} años").grid(row=3, column=1)

Button(root, text="Presioname", command=mostrar_boton).grid(row = 2, column =1 )

root.mainloop()


"""def crear_numero(numero_boton):
    numero =Label(root, text=f"{numero_boton} Pulsado")
    numero.pack()"""

"""boton_1 = Button(root, text="1", command=lambda: crear_numero(1)).pack()
boton_2 = Button(root, text="2", command=lambda:crear_numero(2)).pack()
boton_3 = Button(root, text="3", command=lambda:crear_numero(3)).pack()
boton_4 = Button(root, text="4", command=lambda:crear_numero(4)).pack()
"""