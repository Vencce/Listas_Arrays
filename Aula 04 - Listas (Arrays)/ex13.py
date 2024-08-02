frase = input("Digite uma frase com até 50 caracteres: ")

if len(frase) > 50:
    frase = frase[:50]

contar_brancos = frase.count(' ')
contar_A = frase.upper().count('A')

print(f"Quantidade de espaços em branco: {contar_brancos}")
print(f"Quantidade de vezes que a letra 'A' aparece: {contar_A}")
