#RECURSIVA
def contagem_regressiva_recursiva(n):
    if n <= 0:
        print("Fim da contagem regressiva.")
    else:
        print(n)
        contagem_regressiva_recursiva(n - 1)

n_recursivo = int(input("Digite um número para a contagem regressiva (recursiva): "))

contagem_regressiva_recursiva(n_recursivo)

#ITERATIVA
def contagem_regressiva_iterativa(n):
    while n > 0:
        print(n)
        n -= 1
    print("Fim da contagem regressiva.")

n_iterativo = int(input("Digite um número para a contagem regressiva (iterativa): "))

contagem_regressiva_iterativa(n_iterativo)
