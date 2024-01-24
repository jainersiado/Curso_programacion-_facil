from tkinter import *

root= Tk()

root.title("titulo")

root.geometry("600x450+50+75")

mensaje = Label(text="mensaje 1")
mensaje_2 = Label(text="mensaje 2")

mensaje.grid(row =0 , column=0)
mensaje_2.grid(row =0, column = 1)

root.mainloop()