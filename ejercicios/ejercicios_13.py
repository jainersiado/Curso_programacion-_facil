frase = ["estoy", "aprendiendo", "python", "con", "el", "curso", "de", "programacion", "facil"]

print(" ".join(frase))

colores = ["rojo", "azul", "verde", "amarillo"]
GUION = "-"
PUNTO = "."

for color in colores:
    print("{}{}{}".format(GUION, color.capitalize(), PUNTO))


numero_1 = 10
numero_2 = 34.50
resultado = numero_1 * numero_2

print("la multiplicacion de %i * %.2f da como resultado: %.3f." % (numero_1, numero_2, resultado))

texto = "Muy lejos, más allá de las montañas de palabras, alejados de los países de las vocales y las consonantes, viven los textos simulados. Viven aislados en casas de letras, en la costa de la semántica, un gran océano de lenguas"
contador = 0

letra = input("busque una letra\n")

for i in texto:
    
    if letra in i:
        contador += 1
print(f"se encontro {contador} veces la letra {letra}")



