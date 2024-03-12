# *args y *kwargs
# elementos de python que permiten utilizar un numero indefinido de argumentos en las funciones
# permi



def colores(*color):
    contador = 0
    for i in color:
        contador+= 1
        print(f"color {i} es el numero {contador}")


colores("amarillo", "rojo", "verde")
# como tal solo itera un solo valor que es la tupla

def prueba(*args):
    print(args)

prueba(1,2,3)
#el resultado de los que se pasa a args es que ingresa todo los parametros en una tupla

#kwargs, permite argumentos variables de clave, devuelve un dict se coloca dos asteriscos
#

#use este codigo solo para resumir todo en un solo y reciclar la misma funcion
def diccionario(**kwargs):
    numero = 0
    for clave in kwargs.keys():
        #metodo keys ; solo obtiene las clave de los diccionarios
        numero += 1
        print(f"clave {numero}: {clave}")

    for valor in kwargs.values():
        numero += 1
        print(f"valor {numero}: {valor}")
        #metodo values; solo obtiene el valor del dict
    
    for item in kwargs.items():
        numero += 1
        print(f"diccionario {numero} : {item}")

diccionario(nombre ="jainer", apellidos= "siado", edad = 25)


#combinar argumentos fijos con args

def multiplicar(x,y, *args):
    return x * y * args[0] * args[1] * args[3] 

#en este ejemplo se demuestra como obtener los valores de los args se toman el x = 4, y =, a0= 9 a1= 2 y a 3 = 9 da como resultado 3240 se esta omitiendo un valor ya que no hay algun parametro que no esta siendo ingresado en el return y puedo pasarle los vaalores que quiera el resultado sera el mismo

#tambien si se le pasa la posicion tiene que estar al pasarle los argumentos a la funcion sino dara error
print(multiplicar(4,5,9,2,5,9,10))

def numero_al_cuadrado(*args):
    for i in args:
        print(i * i)

numero_al_cuadrado(4,5,9,10)
    
#usar args junto con kwargs

def combinar(*args, **kwargs):
    print(args)
    print(kwargs)

usuario= {"nombre":"jainer", "edad":27}

combinar(9,10,"jaja", **usuario)
#es imporrtante el orden primero va el args y despues el kwargs(para que este entienada que es un dict se debe colocar un ** al principio como en el ejemplo mostrado)