#importar modulos acceder a bibliotecas de codigo
# modulos : colecciones de codigo para facilitar tareas
# widget componente para añañardir componentes al programa 

from tkinter import *

#crear una ventana grafica(ventana principal)
root = Tk()

#creacion de la etiqueta
mensaje = Label(root, text="mi primer programa con tkinter")

#muestra la etiqueta
mensaje.pack()
#con pack se tiene en cuenta el flujo de ejecuccion de lo que se va a mostrar en el programa

#bucle para que no se cierre la ventana al terminar de leer el codigo
root.mainloop()