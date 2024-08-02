vetor1 = []
vetor2 = []
vetor_intercalado = []

print("Digite os 25 elementos do vetor 1:")
for i in range(25):
    numero = float(input(f"Elemento {i+1}: "))
    vetor1.append(numero)

print("Digite os 25 elementos do vetor 2:")
for i in range(25):
    numero = float(input(f"Elemento {i+1}: "))
    vetor2.append(numero)

for i in range(25):
    vetor_intercalado.append(vetor1[i])
    vetor_intercalado.append(vetor2[i])

print("VETOR INTERCALADO:", ' '.join(f"{num:.2f}" for num in vetor_intercalado))
