# DICCIONARIOS

# diccionario = {"total":55, "desc": True, "subtotal": 45}
# print(diccionario)
"""
diccionario = {}
print(diccionario)

diccionario["nombre"] = "Fernando"
print(diccionario)

valor = diccionario["nombre"]
print(valor)

diccionario["nombre"] = 20
valor = diccionario["nombre"]
print(valor)

print(diccionario)

"""
dic = {"a":1, "b":2, "c":3, "a":4}
print(dic)

resultado = "e" in dic
print(resultado)

resultado = dic.get("a")
print(resultado)

resultado = dic.get("e")
print(resultado)

resultado = dic.get("e", "La llave no existe")
print(resultado)


dic = {"a":1, "b":2, "c":3, "d":4, "e":5}

resultado = dic.keys() #Regresa una tupla de las keys
print(resultado)

resultado = tuple(resultado)
print(resultado)

resultado = list(dic.values())
print(resultado)

resultado = dic.items()
print(resultado)

"""
"""

dic = {"a":1, "b":2, "c":3, "d":4, "e":5}

print(len(dic))
print(dic)

del dic["a"]
print(dic)

valor = dic.pop("b")
print(valor)
print(dic)

dic.clear()
print(dic)

