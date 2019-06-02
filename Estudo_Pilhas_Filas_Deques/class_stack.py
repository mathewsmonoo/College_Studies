#Pilhas,filas,deques:
class Stack:
    __slots__=['itens','__tamanho']

    def __init__(self, tamanho):
        self.itens = []
        self.__tamanho = tamanho

    def size(self):
        return len(self.itens)

    def is_empty(self):
        return self.itens == []

    def is_full(self):
        return len(self.itens) >= self.__tamanho

    def push(self,item):
        if self.is_full() == False:
            self.itens.append(item)
        else:
            print ("erro - pilha cheia")

    def pop(self):
        if self.is_empty():
            return "Pilha vazia!"
        return self.itens.pop()

    def peek(self):
        if self.is_empty() == True:
            return "Pilha vazia!"
        return self.itens[-1]

'''
---------------------------------------------------------------------------------------------------------------------------
Utilização:
---------------------------------------------------------------------------------------------------------------------------
'''
from Pilha import *

if __name__ == "__main__":
    print("ex de pilha")
    
    s = Stack(5)
    print (s.size())
