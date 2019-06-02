class Pokemon():
    __slots__ = ['name', '__HP']
    def __init__(self,name,HP):
        self.name = name    #publico
        self.__HP = HP      #privado

    def __str__(self):
        return("\n\tNome: %s \tHP: %.2f" %(self.name, self.__HP))

    #Getters
    def get_name(self):
        return (self.name,self.__HP)

    def get_HP(self):
        return self.__HP

    # @property
    # def hp(self):
        # return self.__HP

    #Setters
    def set_name(self, e_nome):
        self.name = e_nome

    def set_HP(self, e_HP):
        self.__HP = e_HP


def main():
    print("\n\tIniciando programa....")
    pikachu = Pokemon('Pikachu', 100.0)
    
                            # print("\n\t",pikachu.get_HP(),"\n\t",pikachu.get_name())
                            # e_nome = input("\n\tNome...:")
                            # pikachu.set_name(e_nome)
                            # e_HP = float(input("\n\tHP...:"))
                            # pikachu.set_HP(e_HP)
                            
    print("\n\t",pikachu.get_HP(),"\n\t",pikachu.get_name())
    # pikachu.__HP = 10.0
    # pikachu.hp(10)
    print("Nome: %s" %(pikachu.name))
    print("HP: %.2f" %(pikachu.get_HP()))
    print("HP: %.2f" %(pikachu.__HP))
    
                                # print(pikachu.__dict__)
                                    
                                # print("a: %s , hp: %.2f" %(pikachu.get_name()))


if __name__ == "__main__":
    main()


