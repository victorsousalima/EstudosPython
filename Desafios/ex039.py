an = int(input('Ano de Nascimento: '))
at = 2022

id = at - an

if id >= 19:
    tp = id - 18
    print(f'Já Passou {tp} anos que você devia ter se Alistado ou Seja Já passou o Tempo de se Alistar')
elif id < 18:
    tp = 18 - id
    print(f'Faltam {tp} anos para você se Alistar ou Seja Ainda Vai se Alistar')
elif id == 18:
    print('Está na Hora de se Alistar')
