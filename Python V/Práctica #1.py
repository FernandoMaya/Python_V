"""
numero_1 = 9
numero_2 = 3
numero_3 = 6 
 
media = (numero_1 + numero_2 + numero_3)/ 3 #Los parentesis de la operación.
print("La nota media es ", media) 
"""
"""
nota_1 = 10
nota_2 = 7
nota_3 = 4

nota_final = ((nota_1 * .15) + (nota_2 * .35) + (nota_3 * .50))

print("La nota final es", nota_final)
"""

"""
matriz = [
	[1, 1, 1, 3], 
    [2, 2, 2, 7], 
    [3, 3, 3, 9], 
    [4, 4, 4, 13] 
]
for i in matriz:
	x = slice(3)
	if i[3] != sum(i[x]):
		i[3] = sum(i[x])

print(matriz)
"""
"""
cadena = "zeréP nauJ,01"
print(cadena[::-1] )
"""

"""
base = int(input("Ingrese la base del triangulo: "))

h = int(input("Ingrese la altura del triangulo: "))

area = (base * h)/2

print (area)
"""
"""
dolar = float(input("Ingrese la cantidad a convertir: "))
pesoC = 3784.00

conv = dolar * pesoC
print(conv)
"""
"""
celsius = float(input("Ingresa los grados a convertir: "))

farenheit = (celsius * 1.8) + 32
print(farenheit)
"""
"""
print("Un lustro tiene:",157680000, "segundos")
"""
"""
# 299,792 kilometros por segundo
# 54 600 000 kilómetros
distancia = 54600000
velocidad = 299792
tiempo = (distancia/velocidad)
print("El tiempo que tarda es de", tiempo, "segundos")
"""
"""
llanta = 0.5
dist = 1000
vueltas = (dist/llanta)
print(vueltas)
"""
"""
import math
h = 20
angulo = 22

c_a = math.atan(22) * h

print(c_a)
"""
"""
edad_1 = int(input("Ingresa la primer edad: "))
edad_2 = int(input("Ingresa la segunda edad: "))
bool = False
if edad_1 == edad_2:
	bool = True
	print (bool)
else:
	print (bool)
"""
"""
from datetime import datetime
# d1 = date(input("Ingresa tu fecha de nacimiento: "))
# d2 = date(2020,10,22)
# diff = d2 - d1
# print(diff)
año = int(input("Ingrese su año de nacimiento: "))
mes = int(input("Ingrese su mes de nacimiento: "))
dia = int(input("Ingrese su dia de nacimiento: "))
d1 = datetime(año,mes,dia)
d2 = datetime(2020,10,22)

diff1 = d2 - d1
meses = diff1.days/30
print(str(meses),"Meses")
"""

español = float(input("Ingrese la calificaión de Español: "))
Mate = float(input("Ingrese la calificaión de Mate: "))
Eco = float(input("Ingrese la calificaión de Eco: "))
Progra = float(input("Ingrese la calificaión de Progra: "))
Ingles = float(input("Ingrese la calificaión de Ingles: "))

prom = (español + Mate + Eco + Progra + Ingles)/5

print(prom)