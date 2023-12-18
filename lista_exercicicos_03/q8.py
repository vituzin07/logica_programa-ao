T = [-10, -8, 0, 1, 2, 5, -2, -4]

if not T:
    print("A lista de temperaturas está vazia.")
else:
    menor_temperatura = min(T)
    maior_temperatura = max(T)
    temperatura_media = sum(T) / len(T)
    print(f"Menor temperatura: {menor_temperatura}°C")
    print(f"Maior temperatura: {maior_temperatura}°C")
    print(f"Temperatura média: {temperatura_media:.2f}°C")