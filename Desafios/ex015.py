kmp = float(input('Quantos km você percorreu: '))
qtd = int(input('Quantos dias você usou o carro: '))

pf = (qtd * 60) + (kmp * 0.15)

print('O preço que você irá pagar é de: R${:.2f}'.format(pf))