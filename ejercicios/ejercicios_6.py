#color a una lista con una funcion

colores = ["rojo", "verde", "azul"]

def add_color(color):
    colores.append(color)

add_color(input(" escriba un color para añadir a la lista"))

print(colores)