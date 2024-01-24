#formas de escribir unb string

"string" #comillas dobles
'string' # comillas simples
"'string'"


animal = "perro"

print(animal[1])
print(len(animal)) #solo funciona con str

#convertir int a str
digitos = 16546546
convertidor = str(digitos)

print(len(convertidor))

# convertir str a int y float
numero_a =  "10.25"
numero_b =  "20"

suma = float(numero_a) + int(numero_b)
print(suma)

#convertir decimales a integers
r = 4.4
z = 5.65656
operacion = int(r+z)
print(operacion)
print(round(z))# redondea un numero 
print(round(z, 2)) # se le da el segundo argumento de que tome dos numeros despues de la coma 
operacion_2 = 10 // 3 # devuelve el resultado de una operacion en un int
operacion_3 = 10 / 3
print(operacion_2)
#integer
numero_1 = 100
numero_2 = 200
resultado = numero_1 + numero_2
resultado_2 = numero_1 - numero_2
separador = 546_546_464_646_445_645_646_486_464_564_654_564
float_1 = 56.85

print(resultado)

 #BOOLEAN
verdadero = True
falso = False

print(type(numero_1))
print(type(separador))
print(type(float_1))
print(type(verdadero))

#operacion de incremento

q = 10
q += 10
print(q)

#operacion de decremento
q -= 9
print(q)

#formateo de strings
print(f"el resultado al tener un valor de decremento cambia a {q}")