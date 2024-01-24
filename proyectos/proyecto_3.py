print("CALCULADORA PROGRAMACION FACIL")

operador = input("elija por favor con que operador trabajara \n1- suma \n2- resta \n3- multiplicacion \n4- division \n5- modulo \n6- cociente\n")

numero_1 = float(input("elija un numero:\n "))
numero_2 = float(input("elija otro numero:\n "))

if operador == "1":
    print("Ha elegido la opcion SUMA:")
    print(round(numero_1 + numero_2, 2))
elif operador == "2":
    print("El Resultado es:")
    print(round(numero_1 - numero_2, 2))
elif operador == "3":
    print("El Resultado es:")
    print(round(numero_1 * numero_2, 2))
elif operador == "4":
    print("El Resultado es:")
    print(round(numero_1 / numero_2, 2))
elif operador == "5":
    print("El Resultado es:")
    print(round(numero_1 // numero_2, 2))
elif operador == "6":
    print("El Resultado es:")
    print(round(numero_1 ** numero_2, 2))
else: 
    print("error de opcion intente nuevamente")



