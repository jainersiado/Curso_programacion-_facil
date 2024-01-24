#for i in range(7,15):
 #   print(f"el valor del bucle es: {i}")


#x = 7 

#while x <= 14:
    #print(f"el valor del bucle es {x}")
    #x += 1


#for i in range(0,-5001,-500):
 #   print(i)

#print("\n")

#x = 0

#while x >= -5000:
   # print(x)
    #x -= 500

paises=['Portugal', 'Suiza', 'Alemania', 'Francia', 'Belgica', 'Chile']

for pais in paises:
    print(f"-> {pais} <- ")

lista_numeros = [10, 45, 356, 10, 10, 10 ,46, 67,45, 10, 10, 43, 10, 65, 10, 10]

lista_numeros.sort()

for numero in lista_numeros:
    if numero == 10:
        continue
    elif numero == 356:
        break
    print(numero)