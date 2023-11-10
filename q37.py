tempo_segundos = int(input('Insira o tempo de duração do evento em segundos: '))
Horas = tempo_segundos//3600
tempo_segundos %= 3600
minutos = tempo_segundos//60
segundos = tempo_segundos%60
print(f'Total:{Horas}:{minutos}:{segundos}')