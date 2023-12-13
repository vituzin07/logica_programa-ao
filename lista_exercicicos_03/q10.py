#questão a
def area_quadrado(lado, exibir=False):
    if exibir:
        return lado*lado
x = area_quadrado(4, True), area_quadrado(9, True)
print(x)

#questão b
def area_triangulo (base, altura, exibir=False):
    if exibir:
        return base*altura/2
z = area_triangulo(6, 9, True ), area_triangulo(5, 8, True)
print(z)