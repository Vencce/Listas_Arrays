A = []

for i in range(128):
    numero = float(input(f"Digite o elemento {i+1}: "))
    A.append(numero)

K = float(input("Digite a chave K: "))

if K in A:
    posicao = A.index(K)
    print(f"CHAVE K ENCONTRADA NA POSIÇÃO: {posicao}")
else:
    print("CHAVE K NÃO ENCONTRADA")
