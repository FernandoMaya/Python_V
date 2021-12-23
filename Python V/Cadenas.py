# CADENAS DE CARACTERES
"""
Los strings con cadenas de caracteres con un orden establecido y se trabajan a traves de indices
sub = string[:] Todos los elementos
sub = string[start:] Todos los elementos desde un indice de inicio
sub = string[:end] Todos los elementos desde el inicio hasta el indice indicado como final
sub = string[start:end] Todos los elementos de un rango entre 2 indices
sub = string[start:end:step] Elementos de un rango con un step


lenguajes = "py; java; ruby; php; js; c#; c++"

res = lenguajes.split()
print(res)

res = lenguajes.split("; ")
print(res)

nuevo_str = " ".join(res)
print(nuevo_str)

texto = Esto es un
texto de
varias lineas


resultado = texto.splitlines()
print(resultado)

texto = " taller de python basico basico"
print(texto.capitalize())
print(texto.swapcase())
print(texto.upper())
print(texto.lower())
print(texto.isupper())
print(texto.islower())
print(texto.title())
print(texto.replace("basico", "intermedio", 1))
print(texto.strip())


curso = "Python"
nivel = "Basico"

resultado = "Taller de %s %s" %(curso, nivel)
print(resultado)

resultado = "Taller de {} {}".format(curso, nivel)
print(resultado)

resultado = "Taller de {a} {b}".format(b = nivel, a = curso)
print(resultado)


taller = "Taller de Python"
taller = "t" + taller[1:] + " Basico"
print(taller)
"""

mensaje = "este es un mensaje para ejemplificar las busquedas dentro de otro mensaje"

print(mensaje.count("mensaje"))
print("mensaje" in mensaje)
print("mensaje" not in mensaje)
resultado = mensaje.find("mensaje")
resultado = mensaje[resultado: resultado + len("mensaje")]
print(resultado)
print(mensaje.startswith("Este"))
print(mensaje.endswith("mensaje"))