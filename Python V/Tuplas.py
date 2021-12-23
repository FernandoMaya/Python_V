# TUPLAS
# LAS TUPLAS SON INMUTABLES NO SE PUEDEN EDITAR LOS ELEMENTOS
"""
tupla = (1, 2.5, "Python", [1, 2, 3], (4, 5))
# Rapidez a la hora de consultar los elementos
print(tupla[0])
print(tupla[1])
print(tupla[2])
print(tupla[3])
print(tupla[4])
print(tupla[-1])
print(tupla[-2])
print(tupla[-3])
print(tupla[-4])
print(tupla[-5])

sub = tupla[:] Todos los elementos
sub = tupla[start:] Todos los elementos desde un indice de inicio
sub = tupla[:end] Todos los elementos desde el inicio hasta el indice indicado como final
sub = tupla[start:end] Todos los elementos de un rango entre 2 indices
sub = tupla[start:end:step] Elementos de un rango con un step
"""
"""
tupla = (1, 2, 3, 4, 5, 6)
lista = [10,20,30,40,50,60]
tupla2 = (100, 200, 300) 

res = zip(tupla, lista, tupla2)
print(res)

res = tuple(res)
print(res)

res = list(res)
print(res)
"""
"""
lista = ["Taller", "Python", "Básico"]
tupla = ("listas", "y", "tuplas")
#tupla -> lista
nueva_lista = list(tupla)
print(nueva_lista)

nueva_tupla = tuple(lista)
print(nueva_tupla)
"""
# string -> lista
mensaje = "Este es el curso de Python Básico"
lista_men = list(mensaje)
print(lista_men)
# mensaje.append = ("hola")
# string -> tupla
tupla_men = tuple(mensaje)
print(tupla_men)