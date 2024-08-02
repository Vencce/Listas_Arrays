linhas = 10
colunas = 30

matriz = [[i + j for j in range(colunas)] for i in range(linhas)]

for linha in matriz:
    print(' '.join(f"{elemento:3}" for elemento in linha))
