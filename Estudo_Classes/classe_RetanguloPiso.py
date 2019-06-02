class Retangulo:
	def __init__(self,comprimento = 0 ,largura = 0 ):
		self.comprimento = comprimento
		self.largura = largura
		
	def getcomp(self):
		return self.comprimento
		
	def getlarg(self):
		return self.largura
	
	def	altera_comprimento(self):
		self.comprimento = eval(input("Comprimento...:"))
		
	def altera_largura(self):
		self.largura = eval(input("Largura...:"))
		
	def calc_area(self):
		area = self.comprimento * self.largura
		return area
		
	def calc_perimetro(self):	
		perimetro = 2*(self.comprimento + self.largura)
		return perimetro
	
	def __str__(self):
		return("Largura    : %.2f \n Comprimento: %.2f \n Area       : %.2f \n Perimetro  : %.2f" 
				%(self.largura, self.comprimento,self.calc_area() , self.calc_perimetro()))


def calcula_piso(Obj1,Obj2):
	qtdpisos = Obj1.calc_area() / Obj2.calc_area()
	return qtdpisos

def calc_rodapes(Obj1,Obj3):
	qtdrodapes = (Obj1.getcomp() / Obj3.getcomp())*4
	return qtdrodapes

def alterar_valores(Obj4):
	Obj4.altera_comprimento()
	Obj4.altera_largura()
	
def mainmenu(local,piso,rodape1):
	opcao = 0
	while(opcao != 9):
		print( 50 * "-" )
		print("1 - Medidas do LOCAL")
		print("2 - Medidas do PISO")
		print("3 - Medidas do RODAPE")
		print("4 - Calcular quantidade de pisos")
		print("5 - Calcular quantidade de rodapes")
		print("6 - ALTERAR VALORES")
		print("\n9 - >>>>SAIR<<<<<\n")
		print( 50 * "-" )
		opcao = int(input("Selecione uma opcao:"))
		print ("\n\n")
		if (opcao == 1):
			print("|LOCAL|\n", local,"\n\n")
		elif (opcao == 2):
			print("|PISO|\n",piso,"\n\n")
		elif (opcao == 3):
			print("|RODAPE|\n",rodape1,"\n\n")
		elif (opcao == 4):
			print("|Pisos necessarios|\n", calcula_piso(local,piso),"\n\n")
		elif (opcao == 5):
			print("Rodapes necessarios|\n", calc_rodapes(local,rodape1),"\n\n")
		elif (opcao == 6):
			opcaoobj = int(input("\n 1 - Alterar LOCAL \n 2 - Alterar PISO \n 3 - Alterar Rodape\n"))
			if (opcaoobj == 1):
				alterar_valores(local)
				print("Local alterado com sucesso!")
			elif (opcaoobj == 2):
				alterar_valores(piso)
				print("Piso alterado com sucesso!")
			elif (opcaoobj == 3):
				alterar_valores(rodape1)
				print("Rodape alterado com sucesso!")
			else:
				pass
		else:
			pass

def program_start():
	print("Informe as medidas de um local!")
	alpha   = eval(input("Comprimento............: "))
	beta    = eval(input("Largura................: "))
	local   = Retangulo(alpha,beta)
	
	print("\nInforme as medidas do piso!")
	gamma   = eval(input("Comprimento do piso....: "))
	epsilon = eval(input("Largura do piso........: "))
	piso    = Retangulo(gamma,epsilon)
	
	print("\nInforme a medida do rodapé!")
	zeta    = eval(input("Tamanho do rodape......: "))
	rodape1 = Retangulo(zeta,1)
	
	mainmenu(local,piso,rodape1)

program_start()
sys.exit()
