VET = []

for i in range(20):
    numero = float(input(f"Digite o elemento {i+1}: "))
    VET.append(numero)

VET.sort()

print("VETOR CLASSIFICADO:", ' '.join(f"{num:.2f}" for num in VET))
