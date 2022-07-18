f = str(input('Digite uma Frase: ')).upper().strip()

print('Quantas vezes a Letra A aparece: {}'.format(f.count('A')))
print('Qual Posição a primeira letra A aparece: {}'.format(f.find('A')+1))
print('Qual posição a ultima letra A aparece: {}'.format(f.rfind('A')+1))

