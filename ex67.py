while True:
    valor = int(input('Digite a tabuada que você deseja ver: (números negativos para parar) '))
    if valor < 0:
        break
    print('-' * 30)
    print(f'''              {1}  X {valor} = {valor * 1}
              {2}  X {valor} = {valor * 2}
              {3}  X {valor} = {valor * 3}
              {4}  X {valor} = {valor * 4}
              {5}  X {valor} = {valor * 5}
              {6}  X {valor} = {valor * 6}
              {7}  X {valor} = {valor * 7}
              {8}  X {valor} = {valor * 8}
              {9}  X {valor} = {valor * 9}
              {10} X {valor} = {valor * 10}''')
    print('-' * 30)
print('Programa encerrado.')
