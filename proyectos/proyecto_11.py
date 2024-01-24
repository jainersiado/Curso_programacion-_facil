class  Motocicleta():
    estado = "nueva"
    motor = False  

    def __init__(self, color, matricula,combustible_litros,marca,numero_ruedas,modelo, fecha_fabricacion, velocidad_punta,peso, cilindrada,precio,tope_combustible_litros):
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabicacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
        self.cilindrada = cilindrada 
        self.precio = precio
        self.tope_combustible_litros = tope_combustible_litros

    def arrancar(self):
        if self.motor:
            print("el motor ha arrancado")
        else:
            print("el motor ya esta en marcha")

    def detenerse(self):
        if self.motor:
            print("el motor se ha detenido")
        else:
            print("el motor ya esta detenido, no se puede apagar el motor")

    def valor(self):
        print(f"el precio de la motocicleta es {self.precio}")

    def comprobar_combustible(self):
        
        self.resta =  self.tope_combustible_litros - self.combustible_litros
        print(f"reporte de deposito de gasolina de motocicleta marca {self.marca} modelo {self.modelo} actualemente tiene:\ncombustible actual {self.combustible_litros}LT \ncombustible maximo {self.tope_combustible_litros}LT \nle falta para llenar {self.resta}LT")

    def llenar_tanque(self):
        while True:
            self.cantidad_aplicada = float(input("cuanta cantidad de gasolina desea aplicar:\n"))
        
            if self.combustible_litros + self.cantidad_aplicada <= self.                 tope_combustible_litros:
                self.combustible_litros += self.cantidad_aplicada
                print(f"la cantidad actual de gasolina es {self.combustible_litros}LT")
                break
            else:
                print("esta sobrepasando la cantidad de litros que puede almacenar el tanque")
                print(f"el tope maximo es {self.tope_combustible_litros}LT")


moto_yamaha = Motocicleta("negra", "GMC79E", 10, "Yamaha",2, "FZ 2.0", 2017, 110, 90, 150, 10000,17)


moto_honda = Motocicleta(
    cilindrada= 180,
    peso=110,
    velocidad_punta= 130,
    fecha_fabricacion=2015, 
    modelo="streetfigther", 
    numero_ruedas=2, 
    marca="honda", 
    combustible_litros= 10,
    tope_combustible_litros=20, 
    matricula="JML19G", 
    color= "ROJO",
    precio= 12000
    )


#moto_honda.arrancar()
#moto_honda.detenerse()

#moto_yamaha.arrancar()
#moto_yamaha.detenerse()

#moto_yamaha.valor()


moto_yamaha.llenar_tanque()
