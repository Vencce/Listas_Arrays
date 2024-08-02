matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        elemento = float(input(f"Digite o elemento da linha {i+1}, coluna {j+1}: "))
        linha.append(elemento)
    matriz.append(linha)

k = float(input("Digite a constante k: "))

for i in range(4):
    matriz[i][i] *= k

for linha in matriz:
    print(' '.join(f"{elemento:.2f}" for elemento in linha))
