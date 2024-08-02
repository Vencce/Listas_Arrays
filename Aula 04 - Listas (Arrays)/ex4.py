NOTAS = []

for i in range(30):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    NOTAS.append(nota)

maior_valor = max(NOTAS)
menor_valor = min(NOTAS)
media = sum(NOTAS) / len(NOTAS)
abaixo_da_media = sum(1 for nota in NOTAS if nota < media)

print(f"O maior valor é: {maior_valor:.2f}")
print(f"O menor valor é: {menor_valor:.2f}")
print(f"A média da turma é: {media:.2f}")
print(f"Quantidade de notas abaixo da média: {abaixo_da_media}")
