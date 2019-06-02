#orientação a objetos 

class Point():
#ou class Point(object):
    '''Atributos'''
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        
    '''Metodos'''
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
        
    def getxgety(self):
        print ("\nCoord x: %s" %(self.get_x()))
        print ("Coord y: %s" %(self.get_y()))
        
    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def pontomedio(self,target):
        medio1 = (self.x + target.x)/2
        medio2 = (self.y + target.y)/2
        return Point(medio1, medio2)
        
    def put_xy(self):
        self.x = eval(input("\nX:"))
        self.y = eval(input("Y:"))
        
    def __str__(self):
        return ("(X = %.2f, y = %.2f)" %(self.x, self.y))

'''Main'''
P1 = Point()
print("P1 (endereco): %s" %P1)
P2 = Point()
print("P2 (endereco): %s" %P2)

print("P1 = P2 : (F/V) -->", (P1 is P2))

P1.getxgety()
P2.getxgety()
P1.put_xy()
P2.put_xy()

print("Criando objeto P3:\n")
P3 = Point()
P3.put_xy()
P3.getxgety()

print("Distancia entre P1 e Origem (0,0)...:%5.2d" %P1.distance_from_origin())
print("\nMidpoint:")
P4 = Point()
P4.put_xy()
PM = Point()
PM = P1.pontomedio(P2)
print("|P1 %s|:" %P1)
print("|P2 %s|:" %P2)
print("|P3 %s|:" %P3)
print("|P4 %s|:" %P4)
print("|PM %s|:" %PM)

'''-------------------'''




