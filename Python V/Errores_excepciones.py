# ERRORES

"""
Los errores detienen la ejecución del programa y tienen
varias causas

while(True):
    try:
        n = int(input("Introduce un numero: "))
        m = 4
        print("{}/{} = {}".format(n,m,n/m))
    except:
        print("Ha ocurrido un error")
    else:
        print("Dato correcto")
        break
    finally:
        print("Fin de la iteración")
"""

try:
    n = int(input("Introduce un numero: "))
    5/n
except TypeError:
    print("No se puede dividir el numero entre una cadena")
except ValueError:
    print("Debes introducir una cadena que sea un número")
except ZeroDivisionError:
    print("Ha ocurrido un error por cero")
except NameError:
    print("Ha ocurrido un error, cambia a numero")
except Exception as e:
    print("Ha ocurrido un error no previsto =>", type(e).__name__)
    