from tkinter import *
import os
from PIL import ImageTk, Image 

#acceso a carpetas

#principal
carpeta_principal = os.path.dirname("Curso_python_programacionfacil")


#carpeta imagenes
tkinter = os.path.join(carpeta_principal, "Tkinter")
imag = os.path.join(tkinter, "imagenes")
avatares = os.path.join(imag, "avatars")



root = Tk()
root.configure(background="thistle1")

marco = LabelFrame(root, text="Selecciona Un Usuario:",background="thistle1", border=0)
marco.grid(padx=10, pady=10)

cargar_boton = ImageTk.PhotoImage(Image.open(os.path.join(avatares, "descarga.jpg")).resize((90,50)))

#variable de control




opcion = StringVar()
opcion.set("Error")

def boton_cargado():
    if opcion.get() == "Error":
        Label(root,
              text="NO HA SELECCIONADO NINGUN AVATAR POR FAVOR INTENTELO DE NUEVO!",
              foreground="red2").grid()
    else:
        Label(root,
              text=f"hola {opcion.get()}. Accediendo a tu cuenta personal....").grid()
   
    
#radiobutton y imagenes de avatars

#emma
Radiobutton(marco,
            text="Emma",
            variable=opcion,
            value="Emma",
            background="light blue").grid(row=1, column=0)

cargar_emma = ImageTk.PhotoImage(Image.open(os.path.join(avatares, "emma.png")).resize((150,150)))
mostrar_emma = Label(marco,image=cargar_emma, background="thistle1").grid(row=0, column=0)


#jacob
Radiobutton(marco,
            text="Jacob",
            variable=opcion,
            value="Jacob",
            background="dodger blue").grid(row=1, column=1)

cargar_jacob = ImageTk.PhotoImage(Image.open(os.path.join(avatares, "jacob.jpg")).resize((150,150)))
mostrar_jacob = Label(marco, image=cargar_jacob,background="thistle1" ).grid(row=0, column=1)

#noah
Radiobutton(marco,
            text="Noah",
            variable=opcion,
            value="Noah",
            background="cornflower blue").grid(row=3, column=0)
cargar_noah = ImageTk.PhotoImage(Image.open(os.path.join(avatares, "noah.jpg")).resize((150,150)))
mostrar_noah = Label(marco,image=cargar_noah, background="thistle1").grid(row=2, column=0)

#sophia
Radiobutton(marco,
            text="Sophia",
            variable=opcion,
            value="Sophia",
            background="aquamarine").grid(row=3, column=1)
cargar_sophia = ImageTk.PhotoImage(Image.open(os.path.join(avatares, "sophia.jpg")).resize((150,150)))
mostrar_sophia = Label(marco, image=cargar_sophia, background="thistle1").grid(row=2, column=1)



boton = Button(root,command=boton_cargado,image=cargar_boton, border=0 ).grid()

#bucle de ejecuccion

root.mainloop()