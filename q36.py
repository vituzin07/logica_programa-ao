def calcular_notas(valor):
    notas = [100, 50, 20, 10, 5, 2, 1]
    resultado = {}

    for nota in notas:
        qtd_notas = valor // nota
        if qtd_notas > 0:
            resultado[nota] = qtd_notas
            valor %= nota

    return resultado

valor = int(input("Digite um valor inteiro: "))

notas_calculadas = calcular_notas(valor)

print(f"Valor lido: {valor}")
print("Notas:")
for nota, quantidade in notas_calculadas.items():
    print(f"{quantidade} nota(s) de {nota}")