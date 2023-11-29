distancia = float(input('Insira a distância que deseja percorrer (em KM):'))
preco = ''
if distancia<=200:
    preco = 0.50
    valor = distancia*preco
    print(valor)
if distancia>200:
    preco = 0.45
    valor = distancia*preco
    print(valor)