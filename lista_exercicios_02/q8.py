hora_i = int(input('Insira a hora inicial: '))
minuto_i = int(input('Insira a minuto inicial: '))
hora_f  = int(input('Insira a hora final: '))
minuto_f = int(input('Insira a minuto final: '))
duracao_horas = hora_f - hora_i
duracao_minutos = minuto_f - minuto_i
if duracao_minutos < 0:
    duracao_horas -= 1
    duracao_minutos += 60
if duracao_horas == 0 and duracao_minutos == 0:
    duracao_horas = 24
print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")