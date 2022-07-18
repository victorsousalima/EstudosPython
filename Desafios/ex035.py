l1 = float(input('Primeiro Lado: '))
l2 = float(input('Segundo Lado: '))
l3 = float(input('Terceiro Lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Pode formar um \033[36mTriângulo!')
else:
    print('Não pode formar um \033[31mTriângulo!')
