salario = float(input('Insira seu salário: '))
if salario> 1250.00:
        aumento=salario*10/100
        salario=salario+aumento
        print(salario)
elif salario<= 1250.00:
        aumento=salario*15/100
        salario=salario+aumento
        print (salario)