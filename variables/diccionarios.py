# los diccionarios se almacenan de forma clave valor

animales = {
    # clave(key) : valor(value) 
    "perro" : "canina",
    "gato"  : "felina",
    "caballo": "equina"
    }

print(animales)
print(animales["caballo"])# de esta forma solo se ve el valor de un elemento en concreto

for animal in animales:
    print(f"es un {animal.capitalize()} y pertenece a la familia : {animales[animal]}")
#capitalize pone la primera letra en mayuscula
# el bucle itera en primera instancia las claves en la seguna con los corchetes llama a los valores

# las claves y valores tambien pueden ser numeros
numeros = {
    1: 1999,
    2: 2005,
    3: 44
}

# cambiar el valor de una clave
numeros[3] = 2011

#añadir un valor
numeros[4] = 2016

print(numeros)

#vaciar un diccionario
numeros= {}
