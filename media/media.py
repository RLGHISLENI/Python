####################################################################
### Programa.: media.py                                          ###
### Autor....: Roberto Luis Ghisleni                             ###
### Objetivo.: Ler o nome e as notas do aluno e calcular a média ###
### Versão...: Python 3.7.3                                      ###
####################################################################

# Referências
import os

# Limpa tela antes da execução
os.system('cls')

# Obtem as dados do aluno
nome = input('Informe o nome do aluno: ')
nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))

# Calcula a média
media = (nota1 + nota2) / 2

# Exibe o resultado na tela
print('A média entre {} e {} é igual a {}'.format(nota1, nota2, media))

if media > 6:
    print('Parabéns {} você foi APROVADO!'.format(nome))
else:
    print('Que peninha, você foi REPROVADO {}'.format(nome))

# Executa uma pausa na tela - Maneira 1
#input("Pressione <enter> para continuar")

# Executa uma pausa na tela - Maneira 2
os.system('pause')