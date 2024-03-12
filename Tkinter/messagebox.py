#messagebox es un submodulo de tkinter
#con messagebox se llaman a ventanas con alertas, informacion etc propias del sistema operativo

from tkinter import *
from tkinter.messagebox import *

root = Tk()

root.title("mesaggebox")

def mostrar_info():
    showinfo("Mensaje informativo", "mensaje que sera de caracter informativo al usuario")
    #primero es el titulo despues como segundo argumento el mensaje 

def mostrar_alert():
    showwarning("Cuidado", "mensaje que alerta al usuario de una accion")

def mostrar_error():
    showerror("No es posible", "mensaje que informa de un error al usuario")    

def mostrar_pregunta():
    askquestion("¿sabias que?", "si colocas este messagebox le preguntaras acciones al usuario?")

def mostrar_pregunta_2():
    askyesno("¿sabias que?", "si colocas este messagebox le preguntaras acciones al usuario?")

def mostrar_aceptar_cancelar():
    askokcancel("¿seguro que desea cancelar?", "le preguntaras al usuario de forma especificar si quiere cancelar o continuar?")

def mostrar_si_no_cancelar():
    askyesnocancel("¿quiere copiar este archivo?", "le preguntaras al usuario de forma especificar si quiere hacer algo o no o cancelarlo?")

def mostrar_reintentar():
    askretrycancel("Algo salio mal", "algo que no salio bien y se pregunta al usuario si quiere volver a intentarlo")


Button(root, text="Informativo", command=mostrar_info ).pack()
Button(root, text="alerta", command=mostrar_alert ).pack()
Button(root, text="error", command=mostrar_error ).pack()
Button(root, text="pregunta", command=mostrar_pregunta ).pack()
Button(root, text="Aceptar o cancelar", command=mostrar_aceptar_cancelar ).pack()
Button(root, text="si o no o cancelar", command=mostrar_si_no_cancelar ).pack()
Button(root, text="reintentar", command=mostrar_reintentar ).pack()
root.mainloop()

