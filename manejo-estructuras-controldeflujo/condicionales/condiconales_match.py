

error = input('Introduzca un codigo de error\n')

match error:
    
    case "200":
        print("todo ok")
    case "301":
        print("Movimiento permanente de la pagina.")
    case "302":
        print("movimiento temporal de la pagina")
    case "404":
        print("pagina no encontrada")
    case "500":
        print("error interno del servidor")
    case "503":
        print("servicio no disponible")
    case _:
        print("error no disponible")