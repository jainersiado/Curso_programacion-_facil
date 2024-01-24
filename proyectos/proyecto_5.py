print("pizzeria programacion facil")
nombre = input("intruduce tu nombre\n")
dinero_usuario = float(input(f"introduce tu deposito {nombre}:\n"))
DINERO_TOTAL = dinero_usuario
print(f"{nombre} acabas de ingresar ${dinero_usuario} a nuestra aplicacion")
total = 0
pedido =[]

hawuaina = 7.88
pepperoni = 10
queso_jamon = 5.14



extra_de_queso = 1.25
champiñones = 0.55
salsa = 1

if dinero_usuario <= 0:
    print("valor no valido")

elif dinero_usuario >= queso_jamon:
    while True:
        print("elige tu pizza!!")
        print(f"1 - margarita - {hawuaina}$")
        print(f"2 - pepperoni {pepperoni}$")
        print(f"3 - queso-jamon {queso_jamon}$")

        eleccion = int(input(f"por favor seleccione tu pedido {nombre}´\n"))    

        match eleccion:
            case 1:
                print(f"ha elegido la pizza hawuaina {hawuaina}$ ")
                dinero_usuario -= hawuaina 
                print(f"le quedan {round(dinero_usuario,2)}")
                total += hawuaina
                pedido.append(f" hawuaina - {hawuaina}")
                break
            case 2:
                print(f"ha elegido la pizza pepperoni {pepperoni}$ ")
                dinero_usuario -= pepperoni 
                print(f"le quedan {round(dinero_usuario,2)}")
                total += pepperoni
                pedido.append(f" pepperoni - {pepperoni}")
                break
            case 3:
                print(f"ha elegido la pizza queso-jamon {queso_jamon}$ ")
                dinero_usuario -= queso_jamon 
                print(f"le quedan {round(dinero_usuario,2)}")
                total += queso_jamon
                pedido.append(f" queso-jamon - {queso_jamon}")
                break
            case _:
                print(f"opcion incorrecta {nombre}. seleccion una opcion del 1 al 3")

    print(total)

    while True:
        print("escoja un ingrediente")
        print(f"1 - extra de queso - {extra_de_queso}$")
        print(f"2 - champiñones {champiñones}$")
        print(f"3 - salsa {salsa}$")
        print(f"4 - no añadir nada extra y pagar")

        eleccion = int(input("escoja el numero de su ingredente por favor\n"))

        match eleccion:
            case 1:
                print(f"ha elegido extra de queso {extra_de_queso}$ ")
                dinero_usuario  -= extra_de_queso
                total += extra_de_queso
                print(f"total a pagar {total}$")
                print(f"le quedan {round(dinero_usuario,2)}")
                pedido.append(f"extra de quueso - {extra_de_queso}")
            case 2:
                print(f"ha elegido champiñones {champiñones}$")
                dinero_usuario  -= champiñones
                total += champiñones
                print(f"total a pagar {total}$")
                print(f"le quedan {round(dinero_usuario,2)}")
                pedido.append(f"extra de quueso - {champiñones}")
            case 3:
                print(f"ha elegido {salsa}$ ")
                dinero_usuario  -= salsa
                total += salsa
                print(f"total a pagar {total}$")
                print(f"le quedan {round(dinero_usuario,2)}")
                pedido.append(f"extra de quueso - {salsa}")
            case 4:
                print("de acuerdo, no se añade nada extra")
                break
            case _:
                print(f"opcion incorrecta. seleccion una opcion valida del 1 al 4")

    if total <= DINERO_TOTAL:
        print(f"su pedido señor {nombre}")

        print(f"el total de su pedido es: {total}$")
        print(f"su cambio: {dinero_usuario}")

        for i in pedido:
            print(f"-{i}.")

        print(f"Gracias por tu compra {nombre}")

    else:
        print("\nsu dinero no alcanza para la compra")

else:
    print("ingrese un monto minimo")