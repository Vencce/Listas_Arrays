# Definindo a matriz de produção dos motores M1 e M2
# Matriz de produção 12 x 2 (12 meses x 2 tipos de motores)
producoes = [
    [30, 20],  # Janeiro
    [5, 10],   # Fevereiro
    [7, 15],   # Março
    # ... continuar para os outros meses
    [18, 25]   # Dezembro
]

# Definindo a matriz de custo e lucro para cada tipo de motor
# Matriz 2 x 2 (2 tipos de motores x 2 métricas: custo e lucro)
custos_lucros = [
    [10, 3],   # Custo e lucro do motor M1
    [15, 2]    # Custo e lucro do motor M2
]

# Inicializando as matrizes de resultados
custos_mensais = [0] * 12
lucros_mensais = [0] * 12

# Calculando o custo e o lucro mensal
for i in range(12):
    custos_mensais[i] = producoes[i][0] * custos_lucros[0][0] + producoes[i][1] * custos_lucros[1][0]
    lucros_mensais[i] = producoes[i][0] * custos_lucros[0][1] + producoes[i][1] * custos_lucros[1][1]

# Calculando o custo e o lucro anual
custo_anual = sum(custos_mensais)
lucro_anual = sum(lucros_mensais)

# Impressão dos resultados
print("Custos Mensais:")
for i, custo in enumerate(custos_mensais, start=1):
    print(f"Mês {i}: R$ {custo:.2f} mil")

print("\nLucros Mensais:")
for i, lucro in enumerate(lucros_mensais, start=1):
    print(f"Mês {i}: R$ {lucro:.2f} mil")

print(f"\nCusto Anual: R$ {custo_anual:.2f} mil")
print(f"Lucro Anual: R$ {lucro_anual:.2f} mil")
