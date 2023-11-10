tempo_gasto = float(input('Insira o tempo gasto (horas): '))
velocidade_media = float(input ('Insira  velocidade média (km/h): '))
distancia = tempo_gasto*velocidade_media
litros_necessarios = distancia/12
print(f'{litros_necessarios} km/l')
print(f'{distancia} km')