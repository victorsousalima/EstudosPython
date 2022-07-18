import random

n1 = str(input('Nome do Primeiro Aluno: '))
n2 = str(input('Nome do Segundo Aluno: '))
n3 = str(input('Nome do Terceiro Aluno: '))
n4 = str(input('Nome do Quarto Aluno: '))

lista = [n1, n2, n3, n4]
ae = random.choice(lista)

print('O aluno Escolhido foi: {}'.format(ae))