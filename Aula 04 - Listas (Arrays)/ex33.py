m = 10
n = 10

QUANT = []
print("Digite os elementos da matriz QUANT (10 linhas, 10 colunas):")
for i in range(m):
    linha = [int(input(f"Elemento [{i+1},{j+1}] da matriz QUANT: ")) for j in range(n)]
    QUANT.append(linha)

# a) Somatório dos quadrados da 1ª coluna
soma_quadrados_coluna1 = sum(QUANT[i][0] ** 2 for i in range(m))

# b) Somatório dos cubos da 2ª linha
soma_cubos_linha2 = sum(QUANT[1][j] ** 3 for j in range(n))

# c) Somatório dos elementos da diagonal principal
soma_diagonal_principal = sum(QUANT[i][i] for i in range(m))

# d) Somatório total dos 100 elementos
soma_total = sum(sum(linha) for linha in QUANT)

print(f"Somatório dos quadrados da 1ª coluna: {soma_quadrados_coluna1}")
print(f"Somatório dos cubos da 2ª linha: {soma_cubos_linha2}")
print(f"Somatório dos elementos da diagonal principal: {soma_diagonal_principal}")
print(f"Somatório total dos 100 elementos: {soma_total}")
