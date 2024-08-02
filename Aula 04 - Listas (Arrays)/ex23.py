matriz = []

for i in range(10):
    linha = []
    for j in range(10):
        elemento = int(input(f"Digite o elemento da linha {i+1}, coluna {j+1}: "))
        linha.append(elemento)
    matriz.append(linha)

for linha in matriz:
    print(' '.join(f"{elemento:3d}" for elemento in linha))

soma = 0

for i in range(10):
    for j in range(i + 1):
        soma += matriz[i][j]

print(f"Soma dos elementos abaixo da diagonal principal: {soma}")
