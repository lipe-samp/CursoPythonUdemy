# Operadores de comparação (relacionais)

# OP     Significado:          Exemplos: (True)     Exemplos: (False)
# >      Maior                 2 > 1                1 > 2
# >=     Maior ou igual        2 >= 2               2 >= 3
# <      Menor                 1 < 2                2 < 1
# <=     Menor ou igual        2 <= 2               3 <= 2
# ==     Igual                 'a' == 'a'           'a' == 'c'
# !=     Diferente             'c' != 'b'           'c' != 'c'

maior = 2 > 1
menor = 1 < 2
maior_ou_igual = 3 >= 2
menor_ou_igual = 4 <= 4
igual = 'c' == 'c'
diferente = 'a' != 1

print(maior)

# Se eu digitar no terminal: 
# python -i .\aula19.py
# Eu consigo executar cada variável para saber seu valor, se é True ou False
# Basta digitar o nome da variável após os três símbolos >>>