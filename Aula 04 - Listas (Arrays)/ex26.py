def matriz_produto(A, B):
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    
    C = [[0] * p for _ in range(m)]
    
    for i in range(m):
        for j in range(p):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
    
    return C

m = int(input("Digite o número de linhas da matriz A: "))
n = int(input("Digite o número de colunas da matriz A e o número de linhas da matriz B: "))
A = []
print("Digite os elementos da matriz A:")
for i in range(m):
    linha = []
    for j in range(n):
        elemento = float(input(f"Elemento [{i+1},{j+1}] da matriz A: "))
        linha.append(elemento)
    A.append(linha)

p = int(input("Digite o número de colunas da matriz B: "))
B = []
print("Digite os elementos da matriz B:")
for i in range(n):
    linha = []
    for j in range(p):
        elemento = float(input(f"Elemento [{i+1},{j+1}] da matriz B: "))
        linha.append(elemento)
    B.append(linha)

C = matriz_produto(A, B)

print("Matriz A:")
for linha in A:
    print(' '.join(f"{elemento:.2f}" for elemento in linha))

print("Matriz B:")
for linha in B:
    print(' '.join(f"{elemento:.2f}" for elemento in linha))

print("Matriz C (produto de A e B):")
for linha in C:
    print(' '.join(f"{elemento:.2f}" for elemento in linha))
