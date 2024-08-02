matriz1 = []
matriz2 = []
soma_matriz = []

print("Digite os elementos da primeira matriz 3x5:")
for i in range(3):
    linha = []
    for j in range(5):
        elemento = float(input(f"Elemento [{i+1},{j+1}]: "))
        linha.append(elemento)
    matriz1.append(linha)

print("Digite os elementos da segunda matriz 3x5:")
for i in range(3):
    linha = []
    for j in range(5):
        elemento = float(input(f"Elemento [{i+1},{j+1}]: "))
        linha.append(elemento)
    matriz2.append(linha)

for i in range(3):
    linha_soma = []
    for j in range(5):
        soma = matriz1[i][j] + matriz2[i][j]
        linha_soma.append(soma)
    soma_matriz.append(linha_soma)

print("Matriz resultante da soma:")
for linha in soma_matriz:
    print(' '.join(f"{elemento:.2f}" for elemento in linha))
