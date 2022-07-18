import random

n1 = str(input('Nome do Primeiro Aluno: '))
n2 = str(input('Nome do Segundo Aluno: '))
n3 = str(input('Nome do Terceiro Aluno: '))
n4 = str(input('Nome do Quarto Aluno: '))

lista = [n1, n2, n3, n4]

random.shuffle(lista)

print(lista)