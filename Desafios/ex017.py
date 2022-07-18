import math

co = float(input('Digite o Cateto Oposto: '))
ca = float(input('Digite o Cateto Adjacente: '))

ip = math.hypot(ca, co)

print('O comprimento da Hipotenusa é : {:.2f}'.format(ip))
