materia1 = float(input("Digite a nota da primeira matéria: "))
materia2 = float(input("Digite a nota da segunda matéria: "))
materia3 = float(input("Digite a nota da terceira matéria: "))
faltas = int(input("Digite o número total de faltas: "))

aulas_por_materia = 10
total_aulas = 3 * aulas_por_materia
frequencia = ((total_aulas - faltas) / total_aulas) * 100

aprovado = materia1 > 7 and materia2 > 7 and materia3 > 7 and frequencia >= 75

print("Aluno aprovado?", aprovado)