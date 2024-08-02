matriz = []

for i in range(20):
    linha = []
    for j in range(20):
        elemento = float(input(f"Digite o elemento da linha {i+1}, coluna {j+1}: "))
        linha.append(elemento)
    matriz.append(linha)

for i in range(20):
    diagonal = matriz[i][i]
    for j in range(20):
        matriz[i][j] /= diagonal

for linha in matriz:
    print(' '.join(f"{elemento:.2f}" for elemento in linha))
