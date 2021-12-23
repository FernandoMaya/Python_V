# EJERCICIO 1
"""
calificaciones = {"TOEFL":9, "AdmBD":8, "Adm Redes":9, "Desarrollo web":9, "Desarrollo Movil":9, "Ing. Software":10, "Dispositivos Logicos":8}
print(calificaciones)

resultado = list(calificaciones.values())
print(resultado)
prom = (sum(resultado))/len(resultado)
print(prom)


# EJRECICIO 2
calificaciones = {"TOEFL":9, "AdmBD":8, "Adm Redes":9, "Desarrollo web":9, "Desarrollo Movil":9, "Ing. Software":10, "Dispositivos Logicos":8}

cals = list(calificaciones.values())
mats = list(calificaciones.keys())

mayor = max(cals)
orden = mats[cals.index(mayor)]

print("La materia con mejor calificación es:", orden, "con una calificación de", mayor)

# EJERCICIO 3

lista = []
for i in range(0,9):
  print("Dame el numero ")
  numero = int(input())
  lista.append(numero)
print(lista)
print("La suma de los elementos es:",sum(lista))
print("Numero mayor de la lista es:",max(lista))
print("Numero menor de la lista es:",min(lista))


# EJERCICIO 4

text = []

palabra = input("Ingrese una palabra: ")
text.append(palabra)
while True:
  new = int(input("Ingrese 1 para agregar nueva palabra y 0 para no: "))
  if(new == 1):
    palabra = input("Ingrese una palabra: ")
    text.append(palabra)
  if(new == 0):
    break

for i in text:
    if i == i[::-1]:
      print(i, "Es un palindromo")
    else:
      print(i, "No es un palindromo")


# EJERCICIO 5

frase = input("Ingrese una frase: ")
vocal = 0
for i in frase.lower():
  if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
    vocal += 1
  # return vocal
print (frase)
print(vocal)

# EJERCICIO 6

frase = input("Ingrese una frase: ")
a = 0
e = 0
ii = 0
o = 0
u = 0
for i in frase.lower():
  # if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
  #   vocal += 1
  if i == "a":
    a+= 1
  elif i == "e":
    e += 1
  elif i == "i":
    ii += 1
  elif i == "o":
    o += 1
  elif i == "u":
    u += 1
  # return vocal
print (frase, "salida:", "a:",a,"e:",e,"i:",ii, "o:",o, "u:",u)


# EJERCICIO 7
frase = input("Ingrese una frase: ")
lista = list(frase.lower())
for i in lista:
  if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
    lista.remove(i)
    frase = "".join(lista)
  # return vocal
print (frase)

# EJERCICIO 8

lista = []
for x in range (0, 100, 2):
  lista.append(x)
print(lista)


# EJERCICO 9
minimos = [None, None, None, None, None]
maximos = [None, None, None, None, None]
matriz = [
  [1,2,3,4,5],
  [4,5,6,7,4],
  [3,5,4,3,6],
  [3,4,8,2,6],
  [1,4,3,8,9]
]
print(matriz)
for r in range (0, 5):
  for c in range (0, 5):
    if not(minimos[r]) or minimos[r] > matriz[r][c]:
      minimos[r] = matriz[r][c]
    if not(maximos[c]) or maximos[c] < matriz[r][c]:
      maximos[c] = matriz[r][c]

for r in range (0, 5):
  for c in range (0,5):
    if minimos[r] == maximos[c]:
      print ("punto silla posicion", "Fila", r, "y Columna",c)
"""
# EJERCICIO 10

decimal = int(input("Ingresa un numero en sistema decimal: "))

print("El valor de", decimal, "en los diferentes sistemas es: ")

print(bin(decimal), "en Binario.")

print(oct(decimal), "en Octal.")

print(hex(decimal), "en hexadecimal.")
