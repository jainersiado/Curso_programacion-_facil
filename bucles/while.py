i = 1  # la que iba adentro en el bucle for aca se establece el valor por fuera

while i < 5: #se establece una condicion que si se cumple se ejecuta el bucle 
    print(i)
    i += 1 # se debe establecer el valor de incremento 

x = 1

while x <= 5:
    print(x)
    x += 1


# bucle emulado para do while

while True:
    salida = input("introduce 'salir' para finalizar.\n").lower 
    if salida =="salir":
        break