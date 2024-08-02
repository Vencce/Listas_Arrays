matriz = []

for i in range(15):
    linha = []
    for j in range(25):
        elemento = float(input(f"Digite o elemento da linha {i+1}, coluna {j+1}: "))
        linha.append(elemento)
    matriz.append(linha)

print("MATRIZ:")
for linha in matriz:
    print(' '.join(f"{elemento:.2f}" for elemento in linha))
