from tkinter import *

#creacion de la ventana principal
root = Tk()

#titulo de la ventana
root.title("curso de tkinter en programacion facil")

#tamaño de la ventana
root.geometry("500x400+750+50")

#creacion de las etiquetas
mensaje = Label(root, text="mi primer programa con tkinter").grid(row=0, column=0)#otra forma de mostrar las etiquetas.
mensaje2 = Label(root, text="segunda linea")


#se muestran las etiquetas

mensaje2.grid(row=0, column=1)

#bucle de ejecuccion
root.mainloop()