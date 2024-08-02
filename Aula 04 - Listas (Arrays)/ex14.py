quantidades = []
precos = []

for i in range(100):
    quantidade = float(input(f"Mercadoria {i}: "))
    quantidades.append(quantidade)

for i in range(100):
    preco = float(input(f"Mercadoria {i}: "))
    precos.append(preco)

faturamento = sum(quantidades[i] * precos[i] for i in range(100))

print(f"Faturamento mensal do armazém: {faturamento:.2f}")
