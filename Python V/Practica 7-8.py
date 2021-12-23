import math
import random
class Punto:    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        if x == None:
         self.x = 0
        if y == None:
         self.y = 0
        print("Se ha creado el punto: (",self.x,",", self.y, ") \n")
    def __str__(self):
        return '({} ","{})'.format(self.x, self.y)
    
    #Cuadrante
    def cuadrante (self):
        if self.x == 0 and self.y != 0:
            print("El punto se situa sobre el eje Y \n")
        
        if self.x!= 0 and self.y == 0:
            print("El punto se situa sobre el eje X \n")
        
        if self.x == 0 and self.y == 0:
            print("El punto esta situado en el origen \n")
    
    def vector(self, punto):
        x2 = punto.x
        y2 = punto.y
        
        print("El vector entre: ({},{}) y ({},{})".format(self.x, self.y, x2, y2))
        
        
        
        a = (x2 - self.x)
        b = (y2 - self.y)
        vector = (a,b)
        print("El vector es:", vector, "\n")
    
    def distancia(self, punto):
        x3 = punto.x
        y3 = punto.y
        
        print("La distrancia entre ({},{}) y ({},{})".format(self.x, self.y, x3, y3))
        
        
        resultado = ((x3 - self.x)**2 + (y3 - self.y)**2)
        dist = math.sqrt(resultado)
        
        print ("La distancia es:",dist, "\n")
        return dist


class rectangulo:
    def __init__(self, A, B):
        self.x1 = A.x
        self.y1 = A.y
        self.x2 = B.x
        self.y2 = B.y
        
        if A.x == None:
         self.x1 = 0
        if A.y== None:
         self.y1 = 0
        print("Se ha creado el punto: (",self.x1,",", self.y1, ")")
        
        if B.x == None:
         self.x2 = 0
        if B.y == None:
         self.y2 = 0
        print("Se ha creado el punto: (",self.x2,",", self.y2, ")")
    def __str__(self):
        print('({} ","{})'.format(self.x1, self.y1))
        print('({} ","{})'.format(self.x2, self.y2))
    
    def calc_base (self):
        self.x3 = self.x2
        self.y3 = self.x1
        
        
        a = (self.x3 - self.x1)
        b = (self.y3 - self.y1)
        resultado = (a**2 + b**2)
        dist = math.sqrt(resultado)
        print("La base es:",dist, "\n")
        self.Base = dist
        
    def calc_altura(self):
        c = (self.x3 - self.x2)
        d = (self.y3 - self.y2)
        resultado = (c**2 + d**2)
        h = math.sqrt(resultado)
        print("La altura es:",h, "\n")
        self.Altura = h
    
    def calc_area(self):
        area = self.Base * self.Altura
        print("El area es:",area, "\n")
        
# n = (Punto(-34, None))
# n.cuadrante()
# n.vector(Punto(5,2))
# n.distancia(Punto(3,7))

A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3,-1)
D = Punto(0,0)
A.cuadrante()
B.cuadrante()
C.cuadrante()
A.vector(B)
B.vector(A)
A.distancia(B)
B.distancia(A)

rect = rectangulo(A,B)
rect.calc_base()
rect.calc_altura()
rect.calc_area()

distA = D.distancia(A)
distB = D.distancia(B)
distC = D.distancia(C)

if distA > distB and distA > distC:
    print("El punto A esta mas lejos del origen")

if distB > distA and distB > distC:
    print("El punto B esta mas lejos del origen")

if distC > distA and distC > distB:
    print("El punto C esta mas lejos del origen")
