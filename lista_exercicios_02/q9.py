import random
opcao_computador = random.randint(0, 2)
if opcao_computador == 0:
    escolha_computador = 'pedra'
elif opcao_computador == 1:
    escolha_computador = 'papel'
elif opcao_computador == 2:
    escolha_computador = 'tesoura'

 

opcao_jogador = input("Escolha pedra, papel ou tesoura: ").lower()

# Verifique as condições de vitória do jogador
if (opcao_jogador == 'pedra' and escolha_computador == 'tesoura') or \
   (opcao_jogador == 'tesoura' and escolha_computador == 'papel') or \
   (opcao_jogador == 'papel' and escolha_computador == 'pedra'):
    print("Jogador venceu!")
elif opcao_jogador == escolha_computador:
    print("Empate!")
else:
    print("Computador venceu!")

# Exiba as escolhas do jogador e do computador
print(f"Jogador escolheu {opcao_jogador}")
print(f"Computador escolheu {escolha_computador}")