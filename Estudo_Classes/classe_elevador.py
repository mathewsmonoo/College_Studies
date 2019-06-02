#EX Elevador
class Elevador():
    
    __slots__=['_andar_atual','_total_andares','_capac_elev','_qtd_pessoas']

    def __init__(self, andar = 0, totalandares = 0, capacidade = 0, pessoas = 0):
        self._andar_atual   = andar
        self._total_andares = totalandares
        self._capac_elev    = capacidade
        self._qtd_pessoas   = pessoas

#GETTERS:
    def get_andar(self):
        return self._andar_atual
    def get_totalandares(self):
        return self._total_andares
    def get_capac_elev(self):
        return self._capac_elev
    def get_pessoas(self):
        return self._qtd_pessoas

#SETTERS:
    def set_andar(self,novo_andar):
        self._andar_atual    += novo_andar
    def set_totalandares(self,novo_total):
        self._total_andares  = novo_total
    def set_capac_elev(self,novo_capac):
        self._capac_elev     = novo_capac
    def set_pessoas(self,novo_qtd):
        self._qtd_pessoas    += novo_qtd

#METODOS:
    def inicializar(self,capacidade = 0,totalandares = 0):
        self.set_capac_elev(capacidade)
        self.set_totalandares(totalandares)

    def entrar(self,target):
        total = self.get_pessoas()
        if ((total + 1) > self.get_capac_elev()):
            print('erro')
        else:   
            self.set_pessoas(1)
    
    def sair(self):
        if (self.get_pessoas() > 0):
            self.set_pessoas(-1)
        else:
            print('erro')
    
    def subir(self):
        if ((self.get_andar() +1) > self.get_totalandares()):
            print('erro')
        else:
            self.set_andar(1)

    def descer(self):
        if ((self.get_andar() -1) < 0):
            print('erro')
        else:
            self.set_andar(-1)

    def __str__(self):
        return ("\nAndar: {}\n"
                "Total de Andares: {}\n"
                "Capacidade: {}\n"
                "Pessoas: {}"
                .format(self.get_andar(),self.get_totalandares(),self.get_capac_elev(),self.get_pessoas()))

elevador1 = Elevador()
print(elevador1.__dict__)