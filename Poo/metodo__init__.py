#self  se refiere al objeto instanciado del objeto, representa el propio nombre del objeto
# valores por defecto = atributos de la clase(se especifican solos)
# valores de inicio = atributos de instancia (se los damos en la instanciacion)

class vehiculo:
    
    #atributo de clase: no pertenece a un metodo en especifico pero sigue perteneciendo a la clase
    pais_origen = "alemania"

    #atributo de instancia: que esta dentro de un metodo
                    #parametros
    def __init__(self, color, longitud, ruedas):
        self.color = color
        self.longitud = longitud
        self.ruedas = ruedas
        #atributos = vañpres recibidos de los parametrros

    def mostrar_info(self):
        print(f"vehiculo de color {self.color}. con una longitud de {self.longitud} metros, tiene {self.ruedas} ruedas. viene de {self.pais_origen}")


vehiculo_1 = vehiculo("negro", 5, 4)
camion_1 = vehiculo("verde", 9, 8)
#al instanciar un objeto init se debe poner como argumento todos los parametros designados en el metodo

vehiculo_1.mostrar_info()

