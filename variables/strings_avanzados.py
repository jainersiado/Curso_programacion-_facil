#concatenacion
p = "programacion"
f = "facil"

print(p+f)
print(p,f)#con coma siempre añade un espacio

colores = ["azul", "verde", "amarillo", "rojo"]
separador= ", "

#join
print("".join([p,f]))#por cada valor añade el valor en string que le asignemos es un iterable
print(separador.join(colores))

numero = 4
#%
print("%s %i %s" % (p,numero,f) )#segun el valor que recibe se coloca %f, %i o %d, %s, se debe tener en cuenta el orden 

#format
print("{}".format(f,p,numero))#las llaves remplazan el valor, se ejecutara segun el numero de llaves que se tengan. em este caso solo se muestra uno solo ya que solo se coloca una llave


#dividir strings en varias linbeas
parrafo = """   Lorem "ipsum" dolor sit amet, consectetur adipiscing elit,
 sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
   Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea 
   
   commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"""
#texto preformateado saldra tal cual se coloque en la variables
#de esta forma tambien se puede colocar comillas simples y dobles al mismo tiempo

print(parrafo) 


#multiplicar strings
print(p*3)
print((p+" ")*3)#para aañadir espacios

#iterar un string
for letra in f:
    print(letra)


entrada = input("")
#iterar strings con -range-
for letra in range(len(entrada)):
    print(entrada[letra])

#comprobar si un print esta dentro de otro 
print("cion" in p)#devuelve un booleano dependiendo del resultado

#posicionar o enumerar
print(dict(enumerate(p)))