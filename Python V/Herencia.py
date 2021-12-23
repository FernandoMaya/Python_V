# HERENCIA

class Producto:
    
    def __init__(self, referencia, nombre, precio, descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        
    def __str__(self):
        return f"REFERENCIA\t {self.referencia}\n" \
                f"NOMBRE\t {self.nombre}\n" \
                f"PRECIO\t {self.precio}\n" \
                f"DESCRIPCION\t {self.descripcion}\n"

# HEREDA DE CLASE PRODUCTO POR MEDIO DE LOS PARENTESIS
class Adorno(Producto):
    pass

class Alimento(Producto):
    productor = " "
    distribuidor = " "
    
    def __str__(self):
        return f"REFERENCIA\t {self.referencia}\n" \
                f"NOMBRE\t {self.nombre}\n" \
                f"PRECIO\t {self.precio}\n" \
                f"DESCRIPCION\t {self.descripcion}\n" \
                f"PRODUCTOR\t {self.productor}\n" \
                f"DISTRIBUIDOR\t {self.distribuidor}\n"
                

class Libro(Producto):
    isbn = " "
    autor = " "
    
    def __str__(self):
        return f"REFERENCIA\t {self.referencia}\n" \
                f"NOMBRE\t {self.nombre}\n" \
                f"PRECIO\t {self.precio}\n" \
                f"DESCRIPCION\t {self.descripcion}\n" \
                f"ISBN\t {self.isbn}\n" \
                f"AUTOR\t {self.autor}\n"

adorno = Adorno(123, "Esfera dorada", 5, "Esfera mediana")
# print(adorno)

alimento = Alimento(456, "Botella de agua", 10, "500ml")
alimento.productor = "Ciel"
alimento.distribuidor = "Coca-Cola SA de CV"
# print(alimento)

libro = Libro(789, "Recetas Rapidas", 100, "Recetas Saludables")
libro.isbn = "0-125-5452"
libro.autor = "Desconocido"
# print(libro)

productos = [adorno, alimento, libro]
# print(productos)

# for producto in productos:
#     print(producto, "\n")

# for producto in productos:
#     print(producto.referencia, producto.nombre)

#Ciclo para definir de que instancia es el producto y darle sus argumentos
"""
for producto in productos:
    if (isinstance(producto, Adorno)):
        print(producto.referencia, producto.nombre)
    elif (isinstance(producto, Alimento)):
        print(producto.referencia, producto.nombre, producto.productor)
    elif (isinstance(producto, Libro)):
        print(producto.referencia, producto.nombre, producto.isbn)

# no se usa self fuera de una clase
def rebajar_producto(producto, rebaja):
    producto.precio = producto.precio - (producto.precio/100 * rebaja)
    
print(alimento, "\n")
rebajar_producto(alimento, 3)
print(alimento)

class A:
    
    def __init__(self):
        print("Soy de la clase A")
    
    def a (self):
        print("Método de la clase A")

class B:
    
    def __init__(self):
        print("Soy de la clase B")
    
    def a (self):
        print("Método de la clase B")
#La que esta a la izquierda es la de mayor prioridad en este caso es A
class C(B, A):
    def c(self):
        print("Método de la clase C")
        
c = C()
c.a()
c.b()
c.c()
"""