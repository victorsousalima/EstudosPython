vc = float(input('Qual o Valor da Casa: '))
vs = float(input('Qual o Valor do Sálario: '))
qa = int(input('Quantos Anos vai pagar: '))

qp = vc / (qa * 12)
sa = vs * 0.30

print(f'Valores das Parcelas é de R${qp:.2f}')

if qp > sa:
    print('Emprestimo Negado!')
else:
    print('Emprestimo Aceito')
