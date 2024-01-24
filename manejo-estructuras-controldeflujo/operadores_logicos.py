#and
#true - true son las unicas condiciones que acepta 

color = "rojo" 
forma = "redonda"

if color == "rojo" and forma == "redonda":
    print("la condicion se cumple")

#en este caso no se cumple la condicion pues uno de los dos es false
if color == "rojo" and forma == "cuadrada":
    print("la condicion se cumple")
else: 
    print("la condicion no se cumple")


#or
# false - false es la unica condiciones que no acepta

#en este caso si se cumple la condicion del operador al ser uno de los dos true
if color == "rojo" or forma == "cuadrada":
    print("hay algo erroneo")
else:
    print("todo esta mal")


# not 
# cambia el contrario a las condiciones 

if not color == "azul":
    print("se cumple la condicion ")
else:
    print("no se cumple la condicion")

#el operador and cambia bajo los estander del not
if not(color == "morado" and forma == "triangulo"):
    print("se cumple la condicion bajo el not")
else:
    print("no se cumple la condicion")