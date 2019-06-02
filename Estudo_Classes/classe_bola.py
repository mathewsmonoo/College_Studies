#Classe Bola
#13/3/19 - Mathews Monoo

class Bola:
    def __init__(self, cor = 'incolor', circunf = 0 , material = 'marmore'):
        self.cor = cor
        self.circunf = circunf
        self.material = material
        
    def alterar_cor(self):
        cor = input("Cor da bola:")
        self.cor = cor
    
    def exibir_cor(self):
        print("Cor : %s" %self.cor)
        
    def __str__(self):
        return ("|Cor: %s , \n Circ.: %s , \n Mat.: %s|" %(self.cor, self.circunf, self.material))

def menu1():
    escolha = 3
    while escolha != 0:
        escolha = eval(input("0 para sair,\n1 para alterar cor,\n2 para exibir cor..."))
        if escolha == 1:
            bola1.alterar_cor()
        elif escolha == 2:
            bola1.exibir_cor()
        else:
            print("Comando invalido!")
            continue

alpha = input("|Cor...............:")
beta  = input("|Circunferencia....:")
gamma = input("|Material..........:")
bola1 = Bola(alpha,beta,gamma)
print(bola1)
menu1()


