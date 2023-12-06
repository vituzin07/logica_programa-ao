lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('''F - Adicionar ao fim da fila
A - Atende uma pessoa
S - Sair do sistema\n''')
while True:
    escolha = str(input('''Insira sua escolha:'''))
    if escolha == 'F':
        lista.insert(11, len(lista)+1)
        print(lista)
        print(len(lista))
    elif escolha == 'A':
        del lista[0]
        print(lista)
        print(len(lista))   
    elif escolha == 'S':
        print('Você saiu do sistema.')
        break
    
