# While dentro de While

quantidade_linhas = 5
quantidade_colunas = 5
linha = 1 # linha começa com valor 1 (1º linha)

while linha <= quantidade_linhas:
    coluna = 1 # A coluna precisa voltar a valer 1
    while coluna <= quantidade_colunas:
        print(linha, coluna)
        coluna += 1
    linha += 1
print("Fim")