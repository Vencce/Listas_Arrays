m = 20
n = 30

A = []
print("Digite os elementos da matriz A (20 linhas, 30 colunas):")
for i in range(m):
    linha = [int(input(f"Elemento [{i+1},{j+1}] da matriz A: ")) for j in range(n)]
    A.append(linha)

X = []
print("Digite os elementos do vetor X (30 elementos):")
for i in range(n):
    X.append(int(input(f"Elemento {i+1} do vetor X: ")))

Y = [sum(A[i][j] * X[j] for j in range(n)) for i in range(m)]

print("Matriz A:")
for linha in A:
    print(' '.join(f"{elemento:4}" for elemento in linha))

print("Vetor X:")
print(' '.join(f"{elemento:4}" for elemento in X))

print("Vetor Y:")
print(' '.join(f"{elemento:4}" for elemento in Y))
