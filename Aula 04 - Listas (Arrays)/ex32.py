n = int(input("Digite o número de alunos: "))

X = []
for i in range(n):
    idade = int(input(f"Idade do aluno {i+1}: "))
    sexo = int(input(f"Sexo do aluno {i+1} (0 ou 1): "))
    curso = int(input(f"Curso do aluno {i+1}: "))
    nota = float(input(f"Nota do aluno {i+1}: "))
    X.append([idade, sexo, curso, nota])

melhor_nota = -1
matricula_melhor_nota = -1

for i in range(n):
    if X[i][1] == 0 and X[i][2] == 6:
        if X[i][3] > melhor_nota:
            melhor_nota = X[i][3]
            matricula_melhor_nota = i

if matricula_melhor_nota != -1:
    print(f"Aluno com matrícula {matricula_melhor_nota+1} é do sexo 0, curso 6, e obteve a melhor nota: {melhor_nota:.2f}")
else:
    print("Nenhum aluno do sexo 0 e curso 6 encontrado.")
