import math

a = float(input('Digite o Angulo de um Triângulo: '))

se = math.sin(math.radians(a))
co = math.cos(math.radians(a))
ta = math.tan(math.radians(a))

print('O Seno do ângulo {} é {:.2f}'.format(a, se))
print('O Cosseno do ângulo {} é {:.2f}'.format(a, co))
print('O Tangente do ângulo {} é {:.2f}'.format(a, ta))