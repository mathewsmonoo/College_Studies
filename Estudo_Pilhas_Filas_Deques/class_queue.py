class Queue():
    def __init__(self,lista):
      self.__queue = []
      for value in lista:
        self.__queue.append(value)
        
    def enqueue(self,value):
      self.__queue.append(value)
      
    def dequeue(self):
      if len(self.__queue) > 0:
        return self.__queue.pop(0) 
      else:
        print("ERRO - Fila vazia.")
        return False

    def printme(self):
        if len(self.__queue) <=0 :
            print("ERRO - Fila vazia.")
        else:
            for i in self.__queue:
                print(i)


mylist = []
brbr = Queue(mylist)
brbr.printme()
for i in range (1,10):
    brbr.enqueue(i)
brbr.printme()
for i in range (5):
    brbr.dequeue()
brbr.printme()