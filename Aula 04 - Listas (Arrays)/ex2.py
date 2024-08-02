NOTA = []

for i in range(10):
    nota = float(input(f"Digite a nota {i+1}: "))
    NOTA.append(nota)

media = sum(NOTA) / len(NOTA)

print(f"A média das notas é: {media:.2f}")
