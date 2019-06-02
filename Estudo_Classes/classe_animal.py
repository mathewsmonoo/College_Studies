class Animal(object):
    def __init__(self):
        print("Construindo classe Animal) 

class Mamifero(Animal):
    def __init__(self):
        super().__init__() 
        print(" Construindo classe Mamífero") 

class Cachorro(Mamifero):
    def __init__(self):
        super().__init__()
        print(" Construindo classe Cachorro") 

class Gato(Mamifero):
    def __init__(self):
        super().__init__()
        print(" Construindo classe Gato") 


class Ave(Animal):
    def __init__(self):
        super().__init__()
        print(" Construindo classe Mamífero") 

class Papagaio(Ave):
    def __init__(self):
        super().__init__()
        print(" Construindo classe Papagaio") 


if __name__ == "__main__":




"---------------------------



