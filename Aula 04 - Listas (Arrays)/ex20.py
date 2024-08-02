tabela = []

for i in range(4):
    linha = []
    for j in range(5):
        elemento = float(input(f"Digite o elemento da linha {i+1}, coluna {j+1}: "))
        linha.append(elemento)
    tabela.append(linha)

soma_total = 0

for linha in tabela:
    soma_linha = sum(linha)
    print(f"Soma da linha: {soma_linha:.2f}")
    soma_total += soma_linha

print(f"Soma total de todos os elementos: {soma_total:.2f}")
