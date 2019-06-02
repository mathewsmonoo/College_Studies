class User():
    def __init__(self,fname='firstname',lastname='lastname'):
        self.firstname = fname
        self.lastname  = lastname
        self.age       = 0
        self.login_attempts = 0

    def describe_user(self):
        print("First Name: ", self.firstname)
        print("Last Name : ", self.lastname)
        print("Age       : ", self.age)
    
    def greet_user(self):
        print("Hello, ", self.firstname, " ", self.lastname, " !")

    def increment_login_attempts(self):
        self.login_attempts += 1
        pass
    def reset_login_attempts(self):
        self.login_attempts = 0
        pass
    
    def __str__(self):
        return (" First Name: {} \n Last Name : {} \n Age\t: {} \n LogAttempts: {}".format(self.firstname,self.lastname,self.age,self.login_attempts))


usuario = User()
print(usuario)
#-------------------------------------------------------------------------------------------------------------------------------------------------------

class Veiculo():
    def __init__(self,nome='nome',marca='marca',odometro = 0, ano = 0):
        self.nome = nome
        self.marca = marca
        self.odometro = odometro
        self.ano = ano
#GETTERS
    def get_nome(self):
        return self.nome
    def get_marca(self):
        return self.marca
    def get_odometro(self):
        return self.odometro
    def get_ano(self):
        return self.ano

    def __str__(self):
        return ("Nome      = {}\n"
                "Marca     = {}\n"
                "Odometro  = {}\n"
                "Ano       = {}"
                .format(self.nome,self.marca,self.odometro,self.ano))

class Carro(Veiculo):
    def __init__(self,nome='nome',marca='marca',odometro = 0, ano = 0,portamalas = 0):
        super().__init__(nome,marca,odometro,ano)
        self.tipo = 'CARRO'
        self.portamalas = portamalas

    def __str__(self):
        return super().__str__()  + "\nTipo      = {}\nP. Malas  = {}L".format(self.tipo,self.portamalas)

meuveiculo = Veiculo()
print(meuveiculo,'\n')
meucarro = Carro('599','Ferrari',portamalas = 240)
print(meucarro)
