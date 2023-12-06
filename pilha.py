lista = [1, 2, 3, 4, 5]
print('''E - Empilhar um prato
D - Desempilhar um prato
S - Sair do sistema\n''')
while True:
    escolha = str(input('''Insira sua escolha:'''))
    if escolha == 'E':
        lista.append(len(lista)+1)
        print(lista)
        print(len(lista))
    elif escolha == 'D':
        lista.pop(-1)
        print(lista)
        print(len(lista))   
    elif escolha == 'S':
        print('Você saiu do sistema.')
        break
    