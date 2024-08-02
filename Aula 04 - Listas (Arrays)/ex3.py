NOTA = []

for i in range(10):
    nota = float(input(f"Digite a nota {i+1}: "))
    NOTA.append(nota)

media = sum(NOTA) / len(NOTA)

acima_da_media = sum(1 for nota in NOTA if nota > media)

print(f"A média das notas é: {media:.2f}")
print(f"Quantidade de notas acima da média: {acima_da_media}")
