A = []
for i in range(7):
    elemento = float(input(f"Elemento da linha {i+1} da matriz A: "))
    A.append(elemento)

B = []
for i in range(7):
    elemento = float(input(f"Elemento da linha {i+1} da matriz B: "))
    B.append(elemento)

C = [[A[i], B[i]] for i in range(7)]

for linha in C:
    print(' '.join(f"{elemento:6.2f}" for elemento in linha))
