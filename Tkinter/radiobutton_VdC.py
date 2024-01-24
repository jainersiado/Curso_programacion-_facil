#radio button y variables de control de tkinter
# radiobutton permiten seleccionar varias opciones en el programa como un input type en html

from tkinter import *

#creacion de la ventana
root = Tk()

#titulo de la ventana
root.title("radiobutton")

#VARIABLE DE CONTROL
opcion = IntVar()
opcion.set(2)#con set se puede establecer o cambiar el valor por defecto

def actualiza_radio(valor):
    Label(root, text=valor).pack()

#radiobutton, se puede crear un sistema que agrupe a los radiobutton(variables de control)
#los value se envian a la variable de control
Radiobutton(root,
            text= "rojo",
            variable=opcion,
            value=1
            ).pack()

Radiobutton(root,
            text= "azul",
            variable=opcion,
            value=2
            ).pack()

Radiobutton(root,
            text= "verde",
            variable=opcion,
            value=3
            ).pack()

Radiobutton(root,
            text= "amarillo",
            variable=opcion,
            value=4
            ).pack()

#boton de envio¡
boton_envia = Button(root,
                     text="enviar",
                     command=lambda:actualiza_radio(opcion.get())
                     ).pack()



#bucle de ejecuccion
root.mainloop()

"""
tipos de variables de control de tkinter:
intvar
doublevar
stringvar
booleanvar
"""