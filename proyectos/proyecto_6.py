def suma(numero1 ,numero2):
    return numero1 + numero2
    
def resta(numero1, numero2):
    return numero1 - numero2

def multiplicacion(numero1, numero2):
    return numero1 * numero2

def division(numero1, numero2):
    return numero1 / numero2

def cociente(numero1, numero2):
    return numero1 ** numero2

def modulo(numero1, numero2):
    return numero1 // numero2

while True:
    print("elige la operacion:")
    print("1 - suma")
    print("2 - resta")
    print("3 - multiplicacion")
    print("4 - dividion") 
    print("5 - cociente")
    print("6 - modulo")
    print("7 - salir")

    eleccion = int(input("escoja el numero respectivo a su operacion\n"))
    
    numero1 = int(input("escoja un primer numero\n"))
    numero2 = int(input("escoja un segundo numero\n"))

 
    match eleccion:
        case 1:
            resultado =suma(numero1, numero2)
            print(resultado)
        case 2:
            resultado =resta(numero1, numero2)
            print(resultado)
        case 3:
            resultado = multiplicacion(numero1, numero2)
            print(round(resultado,2))
        case 4:
            resultado = division(numero1, numero2)
            print(round(resultado,2))
        case 5:
            resultado =cociente(numero1, numero2)
            print(round(resultado,2))
        case 6:
            resultado = modulo(numero1, numero2)
            print(round(resultado,2))
        case 7:
            False
        case _:
            print("numero invalido intente de nuevo")
            break

