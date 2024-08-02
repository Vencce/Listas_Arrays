A = []

for i in range(100):
    numero = float(input(f"Digite o valor {i+1}: "))
    A.append(numero)

S = sum(i / A[i] for i in range(100))

contador_menor = sum(1 for i in range(100) if i < A[i])

print(f"S = {S:.2f}")
print(f"Quantidade de termos com numerador menor que o denominador: {contador_menor}")
