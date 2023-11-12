def calcular_idade(dias):
    anos = dias // 365
    meses = (dias % 365) // 30
    dias_restantes = (dias % 365) % 30

    return anos, meses, dias_restantes

idade_em_dias = int(input("Digite a idade em dias: "))

anos, meses, dias = calcular_idade(idade_em_dias)

print(f"A idade é: {anos} anos, {meses} meses e {dias} dias.")
