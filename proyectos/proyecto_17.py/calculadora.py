from operaciones import *


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
            resultado = suma.sumar(numero1, numero2)
            print(resultado)
        case 2:
            resultado =resta.restar(numero1, numero2)
            print(resultado)
        case 3:
            resultado = multiplicacion.multiplicar(numero1, numero2)
            print(round(resultado,2))
        case 4:
            resultado = division.dividir(numero1, numero2)
            print(round(resultado,2))
        case 5:
            resultado =exponente.elevar(numero1, numero2)
            print(round(resultado,2))
        case 6:
            resultado = modulo.modular(numero1, numero2)
            print(round(resultado,2))
        case 7:
            False
            break
        case _:
            print("numero invalido intente de nuevo")
            break
