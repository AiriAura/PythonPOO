class Point():
    def move(self,x,y):
        self.x = x
        self.y = y

    def origin(self):
        self.x = 0
        self.y = 0

    def distance(self, x, y):
        self.x = x*2 
        self.y = y*2
        
#Ejercicio: crear un método que devuelva todos los puntos al origen

p1 = Point()
p2 = Point()

p1.move(4,5)
p2.move(4,6)

print(p1.x,p1.y)
print(p2.x,p2.y)

p1.origin()
p2.origin()

print(p1.x,p1.y)
print(p2.x,p2.y)

