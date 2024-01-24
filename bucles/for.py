#estructusturas de control de flujo que permiten realizar repeticiones en el codigo
# se entra en un bloque de codido mientras dure una determinada condicion


for i in range(5): #variable de control, metodo que devuelve un rango de numeros 
    print(f"el valor del bucle es: {i}\n")
    
    
for i in range(3,6): #establece un rango un rango de numeros
    print(f"el valor del bucle es: {i}")

for x in range(2, 16, 2): #establece el numero de pasos que se dara, tambien se puede hacer con negativos 

    print(f"el numero aumenta de {x}")

colores = ["rojo", "azul", "verde", "amarillo"]

for color in colores:
    if color == "azul" or color == "verde":
        print("se salta estos colores ")
        continue
    print(color)

print("\n")

for colo in colores:
    if colo == "azul":
        print("aqui termina el bucle")
        break
    print(colo)
