import tkinter

root = tkinter.Tk()

root.title("centrado de ventanas")
root.resizable(False, True)
ancho_ventana = 500
alto_ventana = 400

#obtener los tamaños de pàntalla
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()


coordenadas_x = int((ancho_pantalla/2)-(ancho_ventana/2))
coordenadas_y = int((alto_pantalla/2)-(alto_ventana/2))
tkinter.Label(root, text=f"{coordenadas_x}").pack()

root.geometry("{}x{}+{}+{}".format(ancho_ventana, alto_ventana, coordenadas_x, coordenadas_y),)

root.geometry()

#ajustes  ventana y pantalla
#root.eval('tk::PlaceWindow . center')




root.mainloop()
