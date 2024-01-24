from tkinter import *
import os
from PIL import Image, ImageTk
import getpass

#carpeta principal
carpeta_principal = os.path.dirname("Curso_python_programacionfacil")

#carga de imagenes
#icono
icono = os.path.join(carpeta_principal, "imagene")
#imagenes
logo = os.path.join(icono, "paisajes")



usuario_creado = ()


while True:
    
    ingreso_consola = input("dime tu usuario\n")
    ingreso_consola_2 = input("dime tu usuario nuevamente\n")
    contraseña_consola = str(input("dime tu contraeña\n"))
    contraseña_consola_2 = str(input("dime tu contraeña nuevamente\n"))

    if ingreso_consola != ingreso_consola_2 or contraseña_consola != contraseña_consola_2:
        print("datos no coinciden")
    else:
        print("Puede ingresar")
        usuario_creado = (ingreso_consola, contraseña_consola)
        break
        

#ventana principal
root = Tk()

# titulo de la ventana
root.title("Login")

#icono
root.iconbitmap(os.path.join(icono, "favicon.ico"))

#imagenes
logo_tienda = ImageTk.PhotoImage(Image.open(os.path.join(logo, "american-rider.png" )).resize((300, 300)))
mostrar_logo = Label(image=logo_tienda)
mostrar_logo.pack()

#entrada usuario
Label(text="Usuario").pack()
usuario = Entry(root)
usuario.insert(0, "Ej:andrea")
usuario.bind("<Button-1>", lambda x: usuario.delete(0, END))
usuario.pack()

#verifiar usuario
Label(text="Verificar Usuario").pack()
usuario_2 = Entry(root)
usuario_2.insert(0, "debe coincidir")
usuario_2.bind("<Button-1>", lambda x: usuario_2.delete(0, END))
usuario_2.pack()

#entrada contraseña
Label(text="Contraseña").pack()
contraseña = Entry(root)
encriptada = getpass.getpass(contraseña)
contraseña.insert(0, "*"*7)
contraseña.bind("<Button-1>", lambda x: contraseña.delete(0, END))
contraseña.pack()

#verificar contraseña
Label(text="Verifique contraseña").pack()
contraseña_2 = Entry(root)
encriptada_2 = getpass.getpass(contraseña_2)
contraseña_2.insert(0, "*"*7)
contraseña_2.bind("<Button-1>", lambda x: contraseña_2.delete(0, END))
contraseña_2.pack()

def pulsar_boton():
    user = usuario.get()
    user_2 = usuario_2.get()
    password = contraseña.get()
    password_2 = contraseña_2.get()
    if user != user_2 or password != password_2:
         Label(root, text="No PUEDE INGRESAR").pack()
    else:
        Label(root, text="PUEDE INGRESAR").pack()
    
#boton

Button(root, text="Ingresa", command=pulsar_boton).pack()

#cierre de bucle
root.mainloop()