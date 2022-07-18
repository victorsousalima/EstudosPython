time = ('Atlético Mineiro', 'Palmeiras', 'Corinthians', 'Internacional', 'Fluminense', 'Athletico-PR', 'Flamengo',
        'Bragantino', 'São Paulo', 'Santos', 'Botafogo', 'Avaí', 'Goiás', 'Ceará SC', 'Cuiabá', 'Coritiba', 'América-MG',
        'Atlético-GO', 'Fortaleza', 'Juventude')

print('='*40)
print(time[:5])
print('='*40)
print(time[16:])
print('='*40)
print(sorted(time))
print('='*40)
print(f'O time do Coritiba está na {time.index("Coritiba") +1 } o Colocação')