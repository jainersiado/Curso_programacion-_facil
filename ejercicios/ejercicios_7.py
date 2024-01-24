colores = {
    1 : "rojo",
    2 : "azul",
    3 : "verde",
    4 : "amarillo"
}

print(colores)

colores[5] = "morado"
for color in colores:
    print(f"{color} - {colores[color].capitalize()}")