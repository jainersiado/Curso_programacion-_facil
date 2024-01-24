from tkinter import *
import os #Para interactuar con el sistema operativo importar directorios al programa 
from PIL import ImageTk, ImageColor, Image  #procesar las imagenes


#almacanar o cargar directorios
#carpeta principal
carpeta_principal = os.path.dirname(__file__)#el argumento de dirname es la ruta
#se coloca file que es una ruta dinamica puesto que si se coloca file solo se ejecutara en este computo
# la variable file recibe el valor de la ruta desde la cual se carga el archivo que contiene esta variable

#cargar directorio de imagenes
carpeta_imagenes = os.path.join(carpeta_principal, "imagenes")
carpeta_paisajes = os.path.join(carpeta_imagenes, "paisajes")


#creacion de la ventana principal
root = Tk()

#icono de la ventana
root.iconbitmap(os.path.join(carpeta_imagenes, "favicon.ico"))

#carga de imagenes
bosque = ImageTk.PhotoImage(Image.open(os.path.join(carpeta_paisajes, "bosque.jpg")).resize((200,300)))
etiqueta = Label(image=bosque).pack()

root.title("imagenes con programacion facil")

root.mainloop()