# funciones decoradoras permiten decorar el codigo de ciertas funciones. 


def a(b):# "a" es como tal la funcion decoradora  la que se pasara y se coloca arriba con un @
    def c(): # "c" es la funcion interna la que hara el cambio y añadira codigo nuevo  
        b() # "b" es la funcion externa, es la funcion decorada en este caso es sumar este es pasado como parametro a a
        print("hola") # la funcion se guarda a "b" y a este print
    return c # para que pueda ser guardado los cambios se guarda en un return  para poder usar

@a #la funcion decordadora es a , c la funcionalidad y b para este caso es sumar o la externa
def sumar():
    print(10 + 10)


sumar()
# si se coloca el @ la funcion "sumar" estara ligada a la decoradora

def sumar_1(a):
    def uno():
        numero = a() + 1
        return numero
    return uno

@sumar_1
def suma():
    return 2 + 10 + 100

print(suma())

#parametros a las funciones decoradoras
#parametros fijos si solo se necesitan parametros especificos pero solo se podran pasar dos y deben coincidir la funcion decoradora como la decorada
def dos_parametros(b):
    def decoradora(numero1, numero2):
        print("division")
        b(numero1, numero2)
        
    return decoradora

@dos_parametros
def dividir(numero1, numero2):
    print(numero1 / numero2)


#con args y kwargs
# se pueden pasar el numero de parametros que se desee para este caso en especifico se coloca kwargs para que pueda recibir argumentos de clave 
def z(b):
    def decoracion(*args, **kwargs):
        print("multiplicacion")
        b(*args, **kwargs)
    return decoracion

@z
def multiplicar(numero1, numero2 ):
    print(numero1 * numero2)


multiplicar(numero2=2,numero1=10)
dividir(20,10)