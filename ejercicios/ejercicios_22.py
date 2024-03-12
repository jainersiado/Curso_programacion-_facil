def sumar(*args):
    print(args[0]+ args[1] + args[2])

sumar(10,7,5)


def muestra_datos(**kwargs):
    clave = tuple(kwargs.keys())
    valor = tuple(kwargs.values())
    print(f" el {clave[0]} es {valor[0]}, sus {clave[1]} son {valor[1]} y tiene {valor[2]} años de {clave[1]}")    


datos = {"nombre":"javier", "apellidos":"gomez de la barca", "edad":27}

muestra_datos(**datos)