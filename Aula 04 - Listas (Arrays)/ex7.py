VETOR = []

for i in range(200):
    numero = float(input(f"Digite o valor {i+1}: "))
    VETOR.append(numero)

print("Os valores na ordem inversa são:")
for numero in reversed(VETOR):
    print(numero)
