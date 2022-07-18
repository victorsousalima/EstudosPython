p = float(input('Digite o preço do Produto: '))
d = p * 0.05
df = p - d

print('O preço R${} com 5% de desconto é R${:.2f}'.format(p, df))