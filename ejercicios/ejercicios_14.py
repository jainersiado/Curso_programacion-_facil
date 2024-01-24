from tkinter import *
import os
from PIL import ImageTk, ImageColor, Image

#directorio
directorio  = os.path.dirname("Curso_python_programacionfacil")

#carga de imagenes
icono = os.path.join(directorio, "imagene")
imagenes = os.path.join(icono, "paisajes")


print(imagenes)

#ventana principal
root = Tk()

#logo
root.iconbitmap(os.path.join(icono, "favicon.ico"))

#imagenes
imagen_1 = ImageTk.PhotoImage(Image.open(os.path.join(imagenes, "moto-1.jpg")).resize((400,400)))
mostrar = Label(image= imagen_1)
mostrar.grid(row=0, column= 0)

imagen_2 = ImageTk.PhotoImage(Image.open(os.path.join(imagenes, "moto-2.jpg.jpg")).resize((400,400)))
mostrar_2 = Label(image= imagen_2).grid(row=0, column= 1)

imagen_3 = ImageTk.PhotoImage(Image.open(os.path.join(imagenes, "moto-3.jpg.jpg")).resize((400,400)))
mostrar_3 = Label(image= imagen_3).grid(row=1, column= 0)

imagen_4 = ImageTk.PhotoImage(Image.open(os.path.join(imagenes, "moto-4.jpg.jpg")).resize((400,400)))
mostrar_4 = Label(image= imagen_4).grid(row=1, column= 1)

#titulo
root.title("programacion")


#cierre de ejecucion
root.mainloop()