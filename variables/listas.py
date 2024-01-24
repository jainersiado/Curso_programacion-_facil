
lista_colores = ["rojo", "verde", "azul", "amarillo"]

print(lista_colores)

print(f"el color es {lista_colores[0]}")

print(lista_colores[1][0])#del elemento que escojas de la lista elije el elemento escojido

print(lista_colores[-1])#acceder a los valores de forma interna

lista_colores[1] = "morado" #modificar valores de la lista 

lista_colores.append("negro") #añadir elementos al final

lista_colores.insert(2,"marron") #añadir elementos en una posicion especifica

#lista_colores.clear() - metodo para vaciar lista

lista_colores.pop(3) #eliminar un solo elemento segun numero de posiciones

#lista_colores.remove("azul") #elimina un valor de forma especifica

lista_nueva = lista_colores.copy() #se copia la lista tambien se puede reasignar en una variable

lista_colores.count("rojo") # contar numero de veces se repite un elemento

lista_colores.index("marron")#buscar un elemento por posicion, busca la primera ocurrencia

#lista_colores.reverse() #invertir orden de los elementos

lista_colores.sort() #ordernar alfabeticamente si se pone reverse= True lo ordena de manera descendente, tambien lo hace con numeros

lista_colores_2 = ["rosado", "blanco", "beige"]

lista_colores.extend(lista_colores_2) #unir listas 

lista_colores_2.extend("escarlata")


numero = [45,90,54,545,92]

ordenar = numero.sort()

print(ordenar)

