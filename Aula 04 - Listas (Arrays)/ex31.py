m = 20
n = 30

A = []
for i in range(m):
    linha = [int(input(f"Elemento [{i+1},{j+1}] da matriz A: ")) for j in range(n)]
    A.append(linha)

X = []
for i in range(n):
    X.append(int(input(f"Elemento {i+1} do vetor X: ")))

Y = [sum(A[i][j] * X[j] for j in range(n)) for i in range(m)]

for linha in A:
    print(' '.join(f"{elemento:4}" for elemento in linha))

print(' '.join(f"{elemento:4}" for elemento in X))

print(' '.join(f"{elemento:4}" for elemento in Y))
