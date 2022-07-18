from math import trunc
n = int(input('Qual valor para ser sacado: '))

r = n


nota5 = 50
qo = n / nota5
print(f'{trunc(qo)} notas de R$ 50,00')
r = r % nota5

nota2 = 20
qo2 = r / nota2
print(f'{trunc(qo2)} notas de R$ 20,00')
r = r % nota2

nota1 = 10
qo3 = r / nota1
print(f'{trunc(qo3)} notas de R$ 10,00')
r = r % nota1

nota01 = 1
qo4 = r / nota01
print(f'{trunc(qo4)} notas de R$ 1,00')
r = r % nota01

print('Fim!')