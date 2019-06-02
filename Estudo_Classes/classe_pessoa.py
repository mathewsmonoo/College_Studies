class Pessoa():
    def __init__(self,nome = "" ,endereco = ""):
        self.nome = nome
        self.endereco = endereco

    def get_info(self):
        info = "\tNome = %s" %(self.nome)
        info += "\n\t Endereco = %s" %(self.endereco)
        return info

    def __str__(self):
        return self.get_info()


class PessoaFisica(Pessoa):
    def __init__(self,nome,endereco,cpf = ""):
        super().__init__(nome, endereco)
        self.cpf = cpf

    def get_info(self):
        info = super().get_info()
        info += "\n\t CPF:%s" %(self.cpf)
        return info

    def valida_cpf(self):
        print("Validando CPF de %s" %(self.nome))


class PessoaJuridica(Pessoa):
    def __init__(self,nome,endereco,cnpj = ""):
        super().__init__(nome, endereco)
        self.cnpj = cnpj

    def get_info(self):
        info = super().get_info()
        info += "\n\t CNPJ:%s" %(self.cnpj)
        return info

    def valida_cnpj(self):
        print("Validando CNPJ de %s" %(self.nome))


def main():
    alpha = Pessoa("Nome1","Endereco1")
    print(alpha)
    beta = PessoaFisica("Nome2","Endereco2","xCPF")
    print("\n",beta)
    gamma = PessoaJuridica("Nome3","Endereco3","xCNPJ")
    print("\n",gamma)

    try:
        print("\nTentativa de validar o CPF de Alpha (pessoa generica)...\n")
        alpha.valida_cpf()
    except Exception as E:
        print("erro: %s!" %(E))
    finally:
        print()


if __name__ == "__main__":
    main()
    enter = exit()
