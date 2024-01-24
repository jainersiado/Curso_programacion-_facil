#como declarar un metodo en una clase

class vehiculo:
    color = None
    longitud_metros = None
    ruedas = 4

    #metodos
    def arrancar(self):
        print("el vehiculo ha arrancado")

    def detenerse(self):
        print("el vehiculo esta detenido") 
    

vehiculo_1 = vehiculo()
vehiculo_2 = vehiculo()

#llamada a metodos
vehiculo_1.arrancar()
vehiculo_1.detenerse()

# crear atributo nuevo pero solo para ese nuevo objeto perteneciente al objeto principal
vehiculo_2.material_aleron = "fibra de carbono"
print(vehiculo_2.material_aleron)


