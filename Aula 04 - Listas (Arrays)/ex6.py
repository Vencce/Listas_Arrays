A = []

for i in range(100):
    numero = float(input(f"Digite o elemento {i+1}: "))
    A.append(numero)

somatorio = sum(A)

print(f"O somatório dos valores armazenados no vetor é: {somatorio:.2f}")
