# Função para calcular o menor número de notas e moedas possíveis
def calcular_notas_moedas(valor):
    notas_moedas = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01]
    resultado = {}

    for nota_moeda in notas_moedas:
        qtd_notas_moedas = int(valor // nota_moeda)
        if qtd_notas_moedas > 0:
            resultado[nota_moeda] = qtd_notas_moedas
            valor -= qtd_notas_moedas * nota_moeda

    return resultado

# Leitura do valor de ponto flutuante
valor = float(input("Digite um valor monetário (duas casas decimais): "))

# Cálculo das notas e moedas
notas_moedas_calculadas = calcular_notas_moedas(valor)

# Exibição do resultado
print(f"Valor lido: R${valor:.2f}")
print("Notas e moedas:")
for nota_moeda, quantidade in notas_moedas_calculadas.items():
    if nota_moeda >= 1:
        print(f"{quantidade} nota(s) de R${nota_moeda:.2f}")
    else:
        print(f"{quantidade} moeda(s) de R${nota_moeda:.2f}")
