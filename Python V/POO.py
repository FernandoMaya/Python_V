"""
numero = 10
# print(type(numero))

def hola():
    pass
# print(type(hola))

class Galleta:
    pass

una_galleta = Galleta()
otra_galleta = Galleta()

print(una_galleta)
print(otra_galleta)

print(Galleta)

print(type(una_galleta))
print(otra_galleta.__class__)

print(Galleta.__name__)
print(type(una_galleta).__name__)
print(otra_galleta.__class__.__name__)


class Galleta:
    
    chocolate = False
    def __init__(self, sabor, color):
        self.sabor = sabor
        self.color = color
        
    def __str__(self):
        
        return f"Se acaba de hornear una galleta de sabor {self.sabor} y color {self.color} "


galleta = Galleta("Vainilla", "Blanco")
print(galleta)
print(str(galleta))
print(galleta.__str__())


"""
class Pelicula:
    
    # Constructor
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula:", self.titulo)
    
    def __str__(self):
        return '({} , {})'.format(self.titulo, self.lanzamiento)

class Catalogo:
    peliculas = []
    
    def __init__(self, peliculas = []):
        self.peliculas = peliculas
    
    def agreagr(self, p):
        self.peliculas.append(p)
    
    def mostrar(self):
        for p in self.peliculas:
            print(p)
p = Pelicula("El padrino", 170, 1972)
# c = Catalogo([p])
# c.mostrar()
# c.agreagr(Pelicula("El padrino: Parte 2", 200, 1974))
# c.mostrar()


"""
class Ejemplo:
    __atributo_privado = "Atributo inaccesible desde el exterior"

    def __metodo_privado(self):
        print("Metodo inaccesible desde el exterior")
    
    def atributo_publico(self):
        return self.__atributo_privado
    
    def metodo_publico(self):
        return self.__metodo_privado
e = Ejemplo()
print(e.atributo_publico())
print(e.metodo_publico())
"""