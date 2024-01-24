lista_numeros = [10, 45, 55, 76]


print(lista_numeros)

print(lista_numeros[-1])

print(f"el valor mas pequeño en la lista es el {lista_numeros[0]} el mas grande, el {lista_numeros[3]}")

lista_colores = ["rojo", "azul", "verde", "amarillo"]

print(lista_colores[1][2])

lista_colores.insert(0, "gris")
lista_colores.append( "rosa")
lista_colores.insert(3, "naranja")

#recuerda que es las posiciones se mueven
lista_colores.pop(1)
lista_colores.pop(3)
lista_colores.pop(3)

print(lista_colores)

lista_nueva = lista_colores.copy()


numero = [45,90,54,545,92]

numero.sort(reverse=True)

print(numero)