A = int(input('Insira o valor de A: '))
B = int(input('Insira o valor de B: '))
C = int(input('Insira o valor de C: '))
D = int(input('Insira o valor de D: '))
if B>C and D>A and C+D > A+B and C >=0 and D >=0 and A%2==0:
    print('Valores aceitos')
else:
    print('Valores não aceitos')