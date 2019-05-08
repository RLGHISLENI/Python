from pessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self, nome, idade, cnpj):
        super().__init__(nome, idade)
        self.setCNPJ(cnpj)

    def setCNPJ(self, cnpj):
        self.__CNPJ = cnpj

    def getCNPJ(self):
        return self.__CNPJ