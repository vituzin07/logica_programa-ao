numero_1=int(input('Insira o 1º número: '))
numero_2=int(input('Insira o 2º número: '))
numero_3=int(input('Insira o 3º número: '))
if numero_1 > numero_2 > numero_3 :
    print(f'Maior:{numero_1}')
    print(f'Menor:{numero_3}')
elif numero_2 > numero_3 > numero_1 :
    print(f'Maior:{numero_2}')
    print(f'Menor:{numero_1}')
elif numero_3 > numero_1 > numero_2 :
    print(f'Maior:{numero_3}')
    print(f'Menor:{numero_2}') 