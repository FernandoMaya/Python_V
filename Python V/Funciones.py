"""
def saludar():
	print("Hola, este mensaje se llama desde la funcion saludar")

saludar()


def tabla_5():
	for i in range(10):
		print("5 * {} = {}".format(i, i*5))

tabla_5()


def prueba():
	m = 10
	print(m)


m = 20
prueba()
print(m)


def prueba():
	return [1,2,3,4,5]

print(prueba())
print(prueba()[-1])
print(prueba()[1:4])


def prueba():
	return "Una cadena", 30, [1,2,3,4,5]
cadena, numero, lista = prueba()
print(cadena)
print(numero)
print(lista)


def suma(a,b):
	return a + b

def resta(a,b):
	return a - b

resultado = suma(2,3)
print(resultado)

resultado = resta(b = 2, a = 3)
print(resultado)


def resta(a = None,b = None):
	if a == None or b == None:
		print("Error, debes enviar dos numeros")
		return
	return a - b

print(resta(4,6))


def doble(numero):
	return numero * 2

n = 10
n = doble(n)
print(n)


def doble(numeros):
	for i, n in enumerate(numeros):
		numeros[i] *= 2
ns = [10, 20, 30]
doble(ns)
print(ns)


def pindetreminados_pos(*args):
	for arg in args:
		print(arg)

# pindetreminados_pos("Hola", 3, 20, [1,2,3,4,5])

def pindeterminados_nom(**kwargs):
	for kwarg in kwargs:
		print(kwarg,":",kwargs[kwarg])
pindeterminados_nom(n = 5, c = "cadena", l = [1,2])


def cuenta_regresiva(num):
	num-= 1
	if num > 0:
		print(num)
		cuenta_regresiva(num)
	else:
		print("Feliz año nuevo")
	# print("Fin de la función: ", num)

cuenta_regresiva(10)
"""
def factorial(num):
	print("Valor inicial: ", num)
	if num > 1:
		num = num * factorial(num-1)
	print("Valor final:", num)
	return num

print(factorial(3))