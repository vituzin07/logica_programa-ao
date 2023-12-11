# professora deu um problema, quando eu adiciono um a fila, atendo e depois adiciono novamente, o numero se repete. vou deixar o exemplo da saida aqui em baixo:
#Insira sua escolha:F 
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# 11
# Insira sua escolha:A
# [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# 10
# Insira sua escolha:F
# [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11]
# 11
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('''F - Adicionar ao fim da fila
A - Atende uma pessoa
S - Sair do sistema\n''')
while True:
    escolha = str(input('''Insira sua escolha:'''))
    if escolha == 'F':
        lista.append(len(lista)+1)
        print(lista)
        print(len(lista))
    elif escolha == 'A':
        lista.pop(0)
        print(lista)
        print(len(lista))   
    elif escolha == 'S':
        print('Você saiu do sistema.')
        break
    
