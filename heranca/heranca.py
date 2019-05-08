####################################################################
### Programa.: heranca.py                                        ###
### Autor....: Roberto Luis Ghisleni                             ###
### Objetivo.:                                                   ###
### Versão...: Python 3.7.3                                      ###
####################################################################

# Referências
import os
from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica

# Limpa tela antes da execução
os.system('cls')

# Obtem as dados da pessoa física
nomePf = input('Informe o nome da Pessoa Física: ')
idadePf = int(input('Informe a idade: '))
cpf = float(input('Informe o CPF: '))

# Obtem as dados da pessoa jurídica
nomePj = input('Informe o nome da Pessoa Júridica: ')
idadePj = int(input('Informe a idade: '))
cnpj = float(input('Informe o CNPJ: '))

# Constroi os objetos
pf = PessoaFisica(nomePf, idadePf, cpf)
pj = PessoaJuridica(nomePj, idadePj, cnpj)

# Mostra na tela os dados 
print('A Pessoa Física {} possui o CPF {}'.format(pf.getNome(), pf.getCPF()))
print('A Pessoa Jurídica {} possui o CNPJ {}'.format(pj.getNome(), pj.getCNPJ()))

# Executa uma pausa na tela
os.system('pause')

# Referência: https://professormarcolan.com.br/encapsulamento-em-python/