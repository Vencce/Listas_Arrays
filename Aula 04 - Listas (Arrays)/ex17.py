def pesquisa_binaria(vetor, chave):
    esquerda = 0
    direita = len(vetor) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if vetor[meio] == chave:
            return meio
        elif vetor[meio] < chave:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1

A = []

for i in range(128):
    numero = float(input(f"Digite o elemento {i+1}: "))
    A.append(numero)

A.sort()

K = float(input("Digite a chave K: "))

posicao = pesquisa_binaria(A, K)

if posicao != -1:
    print(f"CHAVE K ENCONTRADA NA POSIÇÃO: {posicao}")
else:
    print("CHAVE K NÃO ENCONTRADA")
