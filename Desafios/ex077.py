tp = ('lapis', 'biscoito', 'bolacha', 'tesoura', 'mercado', 'estudar', 'praticar',
      'python', 'futuro', 'programador')

for c in tp:
    print(f'\nNa palavra {c.upper()} tem as vogais ', end='')
    for l in c:
        if l.lower() in 'aeiou':
            print(l, end=' ')
