# # item a
# x = 0
# z = 99
# while x <= z:
#     x = x + 1
#     print(x)
# #item b
# x = 50
# z = 98
# while x <= z:
#     x = x + 2
#     print(x)
#item c
# x = 11
# z = 1
# while x>= z:
#     x = x -1
#     print(x)
#     if x == 0:
#         print('Fogo!')

#item d
par_impar = str(input('Escolha entre ''ímpar'' ou ''par'': '))
limite = int(input('Escolha o limite: '))
num = 1
resultado = []

while num <= limite:
    if par_impar == 'par' and num % 2 == 0:
        resultado.append(num)
    elif par_impar == 'ímpar' and num % 2 != 0:
        resultado.append(num)
    num += 1
if resultado:
    print(f"Números {par_impar} até {limite}: {resultado}")
else:
    print(f"Não há números {par_impar} até {limite}.")