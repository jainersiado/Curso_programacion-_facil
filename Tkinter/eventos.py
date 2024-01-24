#eventos de mouse y teclado: permite que el programa reaccione a pulsar un boton del mouse o una tecla del teclado desencadenando ciertas acciones que se especifiquen en codigo
#estos eventos requieren de una funcion de devolucion
#GUI = INTERFAZ GRAFICA DE USUARIO (UNA VENTANA)

from tkinter import *

#creacion de la ventana pr
root = Tk()

# titulo a la ventana
root.title("Curso pf eventos")

#entrada de datos con un widget desde la misma interfaz
entrada = Entry(root)
entrada.insert(0, "Escribe un nombre")#insertara un texto en el entry primero el indice de donde ira y despues el sting que se mostrara en pantalla.

#metodo bind permite capturar un evento asociar un evento a una funcion
entrada.bind("<Button-1>", lambda x: entrada.delete(0, END))
    #evento boton o tecla:       #controlador llamada a funcion
entrada.pack()

#evento para el boton
def pulsar_boton():
    nombre = entrada.get()#pertenece a la clase entry y almacena los datos obtenidos en entry
    Label(root, text=f"{nombre}").pack()
# las funciones realizan acciones por lo cual un evento es una funcion 
# para cargar el eevento en la misma ventana se puede usar label

# boton
Button(root, text="Presionama!", command=pulsar_boton).pack()
#atributo de tkinter command:asignar o asociar un evento al widget(asocia la funcion con el button)
# los widget se pueden usar sin variable si no es necesario usarlos nuevamente

# bucle de ejecuccion
root.mainloop()