matriz = []
SOMALINHA = []

for i in range(4):
    linha = []
    for j in range(5):
        elemento = float(input(f"Digite o elemento da linha {i+1}, coluna {j+1}: "))
        linha.append(elemento)
    matriz.append(linha)

for linha in matriz:
    soma_linha = sum(linha)
    SOMALINHA.append(soma_linha)

TOTAL = sum(SOMALINHA)

print(f"Total da soma dos elementos de todas as linhas: {TOTAL:.2f}")
4