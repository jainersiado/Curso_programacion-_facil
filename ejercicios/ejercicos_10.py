radio_circulo = int(input("digite el radio"))

PI = 3.1415

(lambda radio : print(round(PI * radio * radio,2))) (radio_circulo) 


(lambda nombre: print(f"hola {nombre}")) ("jainer")


colores = ["rojo", "azul", "verde", "amarillo"]

def mostrar_color():
    print(f"el color de la posicion 1 es {colores[1]}")

mostrar_color()

(lambda color: print(f"la posicion del color en la lista es {colores.index(color)}"))("verde")