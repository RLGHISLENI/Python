from pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade)
        self.setCPF(cpf)

    def setCPF(self, cpf):
        self.__CPF = cpf

    def getCPF(self):
        return self.__CPF