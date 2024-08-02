A = []

for i in range(20):
    numero = float(input(f"Digite o elemento {i+1}: "))
    A.append(numero)

S = sum((A[i] - A[19 - i])**2 for i in range(10))

print(f"S = {S:.2f}")
