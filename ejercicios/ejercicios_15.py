from tkinter import *

root = Tk()

root.title("PROOGRAMACIONFACIL.COM")

marco = LabelFrame(root, width=100, height=110, background="red",border=0)
marco.grid(row=0, column=0)

marco_2 = LabelFrame(root, width=100, height=110, background="yellow",border=0)
marco_2.grid(row= 0, column=1)

marco_3 = LabelFrame(root, width=100, height=110, background="red",border=0)
marco_3.grid(row= 0, column=2)

marco_4 = LabelFrame(root, width=100, height=110, background="yellow",border=0)
marco_4.grid(row= 1, column=0)

marco_5 = LabelFrame(root, width=100, height=110, background="red",border=0)
marco_5.grid(row= 1, column=1)

marco_3 = LabelFrame(root, width=100, height=110, background="yellow",border=0)
marco_3.grid(row= 1, column=2)


#bucle de ejecuccion
root.mainloop()

