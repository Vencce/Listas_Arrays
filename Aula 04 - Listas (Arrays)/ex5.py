VETOR = []

for i in range(100):
    numero = float(input(f"Digite o elemento {i+1}: "))
    VETOR.append(numero)

posicoes = [i for i, numero in enumerate(VETOR) if numero == 30]

if posicoes:
    print(f"O número 30 aparece nas posições: {posicoes}")
else:
    print("O número 30 não foi encontrado no vetor.")
