import random
numero_secreto = random.randint(1, 100)
palpite = 0

while palpite != numero_secreto:
    palpite = int(input("Faça um palpite entre 1 e 100: "))

    if palpite > numero_secreto:
        print("Tente um número menor.")
    elif palpite < numero_secreto:
        print("Tente um número maior.")
    else:
        print(f"Parabéns!! Você acertou o número secreto {numero_secreto}.")
