vetor1 = []
vetor2 = []
vetor3 = []

print("Digite os 10 elementos do vetor 1:")
for i in range(10):
    numero = float(input(f"Elemento {i+1}: "))
    vetor1.append(numero)

print("Digite os 10 elementos do vetor 2:")
for i in range(10):
    numero = float(input(f"Elemento {i+1}: "))
    vetor2.append(numero)

for i in range(10):
    vetor3.append(vetor1[i] + vetor2[i])

print("VETOR 1:", ' '.join(f"{num:.2f}" for num in vetor1))
print("VETOR 2:", ' '.join(f"{num:.2f}" for num in vetor2))
print("VETOR 3:", ' '.join(f"{num:.2f}" for num in vetor3))
