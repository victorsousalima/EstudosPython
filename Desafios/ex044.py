pp = float(input('Preço do Produto: '))
print('[1] A vista no Dinheiro/Cheque \n'
      '[2] A vista no Cartão \n'
      '[3] 2x no Cartão \n'
      '[4] 3x ou mais no Cartão')
op = int(input('Qual opção de pagamento: '))

if op == 1:
      dc = pp - (pp * 0.10)
      print(f'O preço Com 10% de desconto é: R${dc:.2f}')
elif op == 2:
      dc = pp - (pp * 0.05)
      print(f'O preço com 5% de desconto é: R${dc:.2f}')
elif op == 3:
      pc = pp / 2
      print(f'O preço não terá desconto, preço das parcelas: 2x de R${pc:.2f}')
elif op == 4:
      j = pp + (pp * 0.20)
      nm = int(input('Quantas parcelas vão ser: '))
      np = j / nm
      print(f'O preço das Parcelas são: {nm}x de  R${np:.2f}')
      print(f'O preço com 20% de Juros é de: R${j:.2f}')
