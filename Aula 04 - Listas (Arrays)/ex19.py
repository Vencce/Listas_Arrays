matriz = []

for i in range(10):
    linha = []
    for j in range(20):
        elemento = float(input(f"Digite o elemento da linha {i+1}, coluna {j+1}: "))
        linha.append(elemento)
    matriz.append(linha)

linha_quinta = matriz[4]
somatorio = sum(linha_quinta)

print(f"Somatório dos elementos da quinta linha: {somatorio:.2f}")
