#objeto
class Taza():
    color = "blanco" #atributos del objeto
    mensaje = None
    material = "porcelana"
    limpia = True

#instanciar un objeto
taza_1 = Taza()
taza_2 = Taza()

#reasignar valores a atributos de objeto
taza_2.color = "blanco y azul"

print(taza_1)

#como acceder a los atributos de un objeto
print(taza_1.color)

#con pass se puede dejar la clase vacia
class Moto():
    pass
