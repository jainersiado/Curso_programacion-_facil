#PROGRAMACION MODULAR; Forma o tecnica de programar que consiste en dividir un programa grande en diversos modulos o subprogramas, aporta un mayor manejo de codigo mejor legibilidad
#los modulos de un programa pueden ser probados o corregidos de forma individual
# la idea es crear programas con poca dependencia o nula dependencia entre uno y otro

#namespaces
#scopes es la zona del codigo en la que es accesible un elemento

import math
import resta #este modulo es el creado en el archivo resta, de esta forma se cran los modulos y se llaman

sustracion = resta.restar(4,5)
print(sustracion)


calculo_1 = math. pow(2,7)

def pow(numero1, numero2):
    return numero1 ** numero2

calculo_2 = pow(2,7)
print(calculo_2)
print(calculo_1)





nombre = "programacion facil"#alcance global


def Imprimir_nombre():
    nombre = "PCMaster"#alcance local
    return nombre

Imprimir_nombre()

print(nombre)

#scopes:
# "nombre" de la funcion no se reasigna el valor ya que el segundo al estar dentro del alcance de la funcion no entra en el scope global del programa ni se puede llamar sin la funcion por las mismas razones

#namespaces son las fronteras del codigo, para no llamar a los elementos con el mismo nombre

#alcance de bloque; afecta a los bucles y condicionales 
#ejemplo:
valor = 1

if valor == 1:
    resultado = 10 + 10
    print(resultado)
else:
    print("nada")

print(resultado)
#el programa no tendra error si el "resultado" es true en este caso pero si es un else si ya que resultado pertenece o es declarado en el el if lo mejor seria colocarlo en el alcance global
#no seria optimo acceder a "resultado" desde el scope local-en este caso el if- hacia el scope global ya que si en este caso es un else dara error el programa