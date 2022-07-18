l1 = float(input('Primeiro lado: '))
l2 = float(input('Segundo lado: '))
l3 = float(input('Terceiro lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Pode formar um Triângulo!')
    if l1 == l2 and l2 == l3:
        print('É um triângulo Equilátero!')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('É um triângulo Isósceles!')
    elif l1 != l2 or l2 != l3 or l1 != l3:
        print('É um triângulo Escaleno!')
else:
    print('Não pode formar um Triângulo!')