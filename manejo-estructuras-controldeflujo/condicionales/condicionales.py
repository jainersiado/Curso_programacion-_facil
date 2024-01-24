# > mayor que
# < menor que
# == igual que
# >= mayor o igual que
# <= menor o igual que
# != diferente que

numero = 8

if numero > 8:
    print("numero es mayor que 8")
elif numero == 8:
    print("el numero es igual a 8 ")
else: 
    print("el numero  es menor a 8")



edad = int(input("introduzca su edad:\n "))

respuesta = None

if edad >= 18:
    print(" es mayor de edad, puede comprar alohol. eliga cual desea ")
    respuesta = input("1- ron.\n2- whisky\n3- ginebra. \n")

    if respuesta == "1":
        print("ha elegeido comprar ron")
    elif respuesta == "2":
        print("ha elegeido comprar whisky")
    elif respuesta == "3":
        print("\nha elegeido comprar ginebra")
    else: 
        print("opcion no valida")





else: 
    print("no se nos permite vender a menores de edad")




