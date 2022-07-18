f = str(input('Digite um frase: ')).upper().strip()
p = f.split()
j = ''.join(p)
i = j[::-1]
print(i, j)
if i == j:
    print('é um Palíndromo!')
else:
    print('não é um Palíndromo!')
