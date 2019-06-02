class PriorityQueue():
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
           print ("erro - fila cheia")

   def pop(self):
       if self.is_empty():
           return "Fila vazia!"
       return self.itens.pop()

   def peek(self):
       if self.is_empty():
           return "Fila vazia!"
       indice = self.__find_item()
       return self.itens[indice]

   def enqueue(self,item,prioridade):
       if self.is_full():
           print("Fila cheia!")
       else:
           entrada = NewEntry(item,prioridade)
           self.itens.append(entrada)

   def dequeue(self):
       if self.is_empty():
           return "Fila Vazia!"
       indice = self.__find_item()
       return self.itens.pop(indice)
  
   def __find_item(self):
       maior_prioridade = self.itens[0].prioridade
       indice = 0
       for i,entrada in enumerate(self,itens):
           if entrada.prioridade < maior_prioridade:
               maior_prioridade = entrada.prioridade
           indice = i
          
   def __str__(self):
       return ("Item:{}\nTamanho {}".format(str(self.itens()),self.size()))
           
class NewEntry():
   def __init__(self,item,prioridade):
       self.item = item
       self.prioridade = prioridade
  
   def __str__(self):
       return self.item
      
      
'''
---------------------------------------------------------------------------------------------------------------------------
Utilização:
---------------------------------------------------------------------------------------------------------------------------
'''

if __name__ == "__main__":
   print("ex de fila")
   minhafila = PriorityQueue(5)
   minhafila.enqueue('Item1',1)
   print(minhafila)
  

