def suma(a,b):
    try:
        result = a + b
    except TypeError:
        print("Error: Tipo de dato no válido")
    else:
        return result

def resta(a,b):
    try:
        result = a - b
    except TypeError:
        print("Error: Tipo de dato no válido")
    else:
        return result

def producto(a,b):
    try:
        result = a * b
    except TypeError:
        print("Error: Tipo de dato no válido")
    else:
        return result

def division(a,b):
    try:
        result = a / b
    except TypeError:
        print("Error: Tipo de dato no válido")
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero")
    else:
        return result