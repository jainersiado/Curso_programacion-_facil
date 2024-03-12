#crear metodos init con valores con defectos
#de esta forma si hay un atributo que no se le pase al metodo init, no dara error sino que lo remplaza con estos valores por defecto
# los argumentos posicionales no se pueden pasar al final solo al principio y si son obligatorios pasarlos

class Usuario:
    def __init__(self,telefono, nombre = "", apellidos = "", edad= 0):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.telefono = telefono

    def describe(self):
        print(f"nombre {self.nombre}")
        print(f"Apellidos {self.apellidos}")
        print(f"edad {self.edad}")
        print(f"telefono {self.telefono}")

usuario_1 = Usuario(320545495) #se mostraran los valores por defecto aunque no se este pasando nada, el unico valor que es obligatorio pasarle es el telefono
usuario_2 = Usuario(edad=24, nombre="Stanly",  telefono=3043136951) # se pasan los argumentos de clave en el orden que se desee sin embargo no afectara el programa y se cambian correctamente, tambien se demuestra que con argumento de clave se puede poner donde se quiera sin embargo sigue siendo obligatorio pasar el valor


usuario_1.describe()
usuario_2.describe()