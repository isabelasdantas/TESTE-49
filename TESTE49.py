escolha = int(input('Escolha um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} X {:2} = {}'.format(escolha, c, escolha*c))
