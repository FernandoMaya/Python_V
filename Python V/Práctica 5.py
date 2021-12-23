import math

salir = False
opc = 0

while not salir:
	opc = int(input("1. Ejercicio #1, 2.Ejercicio #2, 3. Ejercicio #3, 4. Ejercicio #4, 5. Ejercicio #5, 6. Ejercicio 6, 0. Salir: "))

	if opc == 1:
		def area_rectangulo(base,altura):
			return base * altura

		resultado = area_rectangulo(15,10)
		print(resultado)

	elif opc == 2:
		def area_circulo(radio):
			return (math.pi * radio**2)
		area = area_circulo(5)
		print(area)
	elif opc == 3:
		def relacion(x,b):
			if x > b:
				return 1
			if x < b:
				return -1
			if x == b:
				return 0
		num1 = relacion(5,10)
		num2 = relacion(10,5)
		num3 = relacion(5,5)
		print("Relacion 1:",num1)
		print("Relacion 2:",num2)
		print("Relacion 3:",num3)
	elif opc == 4:
		def intermedio(b,c):
			return (b + c)/2
		inter = intermedio(-12,24)
		print("El punto medio es:", inter)
	elif opc == 5:
		def recortar(numero, minimo, maximo):
			if numero < minimo:
				return minimo
			if numero > maximo:
				return maximo
			if numero > minimo and numero < maximo:
				return numero
		limite = recortar(15,0,10)
		print(limite)
	elif opc == 6:
		def separar(lista):
			pares = []
			impares = []
			for i in lista:
				if i % 2 == 0:
					pares.append(i)
				else:
					impares.append(i)
			print(pares)
			print(impares)
		separar([-12, 84, 13, 20, -33, 101, 9])
	elif opc == 0:
		salir = True
	else:
		print("Numero incorrecto, elija uno del menu")