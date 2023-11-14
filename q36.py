# def calcular_notas(valor):
#     notas = [100, 50, 20, 10, 5, 2, 1]
#     resultado = {}

#     for nota in notas:
#         qtd_notas = valor // nota
#         if qtd_notas > 0:
#             resultado[nota] = qtd_notas
#             valor %= nota

#     return resultado

# valor = int(input("Digite um valor inteiro: "))

# notas_calculadas = calcular_notas(valor)

# print(f"Valor lido: {valor}")
# print("Notas:")
# for nota, quantidade in notas_calculadas.items():
#     print(f"{quantidade} nota(s) de {nota}")

Valor = int(input("Insira um valor inteiro: "))
Nota_100 = 100
Nota_50 = 50
Nota_20 = 20
Nota_10 = 10
Nota_5 = 5
Nota_2 = 2
Nota_1 = 1
quantidade_notas = 0
if Valor >= Nota_100:
    quantidade_notas = Valor//Nota_100
    print(f"{quantidade_notas} nota(s) de R$ {Nota_100}")
elif Valor >= Nota_50:
     resto_de100 = Valor%Nota_100
     resto_de100//Nota_50