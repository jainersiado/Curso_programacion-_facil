from tkinter import *
#estilo y personalizacion
#los widget tienen atributos y con esto se pueden personalizar
#frame o marcos , sirven para crear seciones y estructurar


#ventana principal
root = Tk()

#titulo
root.title("Estilos y marcos")

#si no le añades estilos o contenido no aparecera(marco)
marco = LabelFrame(root,
                   text="Marco en la ventana principal",
                   padx= 35,
                   pady= 35)
marco.pack(padx=30, pady=30)

#si se tiene mas marcos se especifica en que marco va ese widget
marco_2 = LabelFrame(root,
                   text="Enviar",
                   padx= 35,
                   pady= 35)
marco_2.pack(padx=30, pady=30)

marco_3= LabelFrame(root,
                   text="Resultado",
                   padx= 20,
                   pady= 20)
marco_3.pack(padx=5,pady=15)

#entrada de datos
entrada = Entry(marco,
                background="springgreen",
                border=3,
                foreground="red",
                width=30,
                )
entrada.insert(0,"escriba su nombre")
entrada.bind("<Button-1>", lambda x: entrada.delete(0, END))
entrada.pack()

def enviar():
    nombre =entrada.get()
    Label(marco_3,
          text=nombre,
          background="skyblue",
          width=26,
          ).pack()

boton = Button(marco_2, 
               text="Enviar", 
               command=enviar,
               background="deepskyblue",
               foreground="gray98",
               border=3,
               width=25,
               ).pack()

root.mainloop()