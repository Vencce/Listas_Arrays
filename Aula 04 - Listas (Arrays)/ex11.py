vetor1 = []
vetor2 = []

for i in range(10):
    numero = float(input(f"Digite o elemento {i+1}: "))
    vetor1.append(numero)

for i in range(10):
    if i % 2 == 0:
        vetor2.append(vetor1[i] * 3)
    else:
        vetor2.append(vetor1[i] / 2)

print("VETOR 1:", ' '.join(f"{num:.2f}" for num in vetor1))
print("VETOR 2:", ' '.join(f"{num:.2f}" for num in vetor2))
