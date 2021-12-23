
try:
    resultado = 10/0
except ZeroDivisionError:
    print("Ha ocurrido un error por cero")
    print("Cambie el 0 por un numero diferente")

"""
try:
    lista = [1, 2, 3, 4, 5]
    lista[10]
except IndexError:
    print("La lista no tiene indice 10, unicamente indices del 0 al 4")


try:
    colores = {'rojo':'red', 'verde':'green', 'negro':'black' }
    colores['blanco']
except KeyError:
    print("La llave blanco no se encuentra en el diccionario")
"""
"""
try:
    resultado = 15 + "20"
except TypeError:
    print("Para realizar la operacion cambie todos los valores a un entero (int)")

"""
"""
def agregar_una_vez(lista,el):
    if el not in lista:
        lista.append(el)
    else:
        raise ValueError ("Error: Imposible añadir elementos duplicados => {}".format(el))
    print(lista)
        
elementos = [1, 5, -2]
agregar_una_vez(elementos, -2)
"""