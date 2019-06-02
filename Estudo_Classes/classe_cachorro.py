class Cachorro():
    __slots__=['__nome','__raca']       #Limitando atributos

    def __init__(self,nome = 'nome',raca = 'raca'):
        self.__nome = nome
        self.__raca = raca
        
    @property                    #getter ----------> 1x property e 1x atr.setter para cada attr.
    def nome(self):              #Returns Cachorro nome
        return self.__nome
    @nome.setter                 #setter
    def nome(self,nome):        #Sets Cachorro nome to nome2
        self.__nome = nome

    @property
    def raca(self):            #Returns Cachorro Raca
        return self.__raca  
    @raca.setter    #setter
    def raca(self,raca2):        #Sets Cachorro Raca to raca2
        self.__raca = raca2
    def __str__(self):
        return ("Nome: {}\nRaça: {}".format(self.nome, self.raca))
                                            #como têm-se decorators, utilizar <self.atr>

tinuco = Cachorro('tinuco','rott')
