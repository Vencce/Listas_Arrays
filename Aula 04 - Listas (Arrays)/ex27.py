estoque = [
    [1200, 3700, 3737],
    [1400, 4210, 4224],
    [2000, 2240, 2444]
]

custos = [260.00, 420.00, 330.00]

num_armazens = len(estoque)
num_produtos = len(custos)

for i in range(num_armazens):
    total_itens = sum(estoque[i])
    print(f"Armazém {i+1}: {total_itens} itens")

quantidade_produto2 = [estoque[i][1] for i in range(num_armazens)]
max_quantidade = max(quantidade_produto2)
armazem_max_produto2 = quantidade_produto2.index(max_quantidade) + 1
print(f"Armazém com a maior quantidade do Produto 2: Armazém {armazem_max_produto2}")

print("Custo de cada produto em cada armazém:")
for i in range(num_armazens):
    custos_armazem = [estoque[i][j] * custos[j] for j in range(num_produtos)]
    print(f"Armazém {i+1}: {custos_armazem}")

print("Custo total de estoque em cada armazém:")
for i in range(num_armazens):
    custo_total_armazem = sum(estoque[i][j] * custos[j] for j in range(num_produtos))
    print(f"Armazém {i+1}: R$ {custo_total_armazem:.2f}")

print("Custo de cada produto em todos os armazéns:")
for j in range(num_produtos):
    custo_total_produto = sum(estoque[i][j] * custos[j] for i in range(num_armazens))
    print(f"Produto {j+1}: R$ {custo_total_produto:.2f}")
