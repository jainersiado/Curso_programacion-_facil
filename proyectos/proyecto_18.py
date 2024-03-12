import random
from tkinter import *
import tkinter.messagebox as msb

aleatorio = random.randint(0,1000)

#codigo de logica para el programa
"""
intentos = 0

numero_usuario = int(input("introduce un numero para adivinar el numero secreto \n"))

print(aleatorio)
while True:
    if numero_usuario < aleatorio:
        print("el numero es menor al deseado")
        numero_usuario = int(input("intentelo de nuevo"))
        intentos += 1
    elif numero_usuario > aleatorio:
        print("el numero es mayor al deseado")
        numero_usuario = int(input("intentelo de nuevo"))
        intentos += 1
    else:
        print(f"excelente lo has logrado te tomo {intentos} intentos")
        break"""

#inicio
root = Tk()

#titulo
root.title("JUEGO DE AZAR")

#ajistes de pantalla
root.resizable(False,False)
root.attributes("-topmost", True)
root.eval('tk::PlaceWindow . center')

#entrada
entrada = Entry(root)
entrada.insert(0, "ingresa un numero")
entrada.bind("<Button-1>", lambda x: entrada.delete(0, END))
entrada.pack()

intentos = 0
numero_aleatorio = random.randint(0,1000)
print(numero_aleatorio)

msb.showinfo("Adivina el número.", "Introduzca un número del 0 al 1000. ¿Cuántos intentos necesitará para conseguir acertar el número secreto?")

def para_boton():
    
    global intentos
    
    try:
        entrada_guardada = int(entrada.get())

        if entrada_guardada < numero_aleatorio:
            msb.showinfo("FALLASTE", "Intentalo con un numero mayor")
            intentos += 1
        elif entrada_guardada> numero_aleatorio:
            msb.showinfo("FALLASTE", "intentalo con un numero menor")
            intentos += 1
        else:
            msb.showinfo("EXCELENTE", f"lo has logrado te tomo {intentos} intentos")

    except:
        msb.showerror("¡ERROR!","Valor no valido intente ingrresando numeros")

#boton
boton = Button(root, text="PLAY", command=para_boton).pack()


#cirerre de bucle de ejecuccion
root.mainloop()
