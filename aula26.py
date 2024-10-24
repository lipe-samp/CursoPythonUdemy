# Caractere  (<) (^) (>)
# (>) - Esquerda
# (^) - Centro
# (<) - Direita

# Sinal: (+) ou (-)
# Exemplo do sinal: 0>-100,.1f

# Conversion flags: (!r) (!s) (!a) >>>> Mais pra frente irá explicar como trabalhar com as flags

variavel = 'ABCD'
print(f'{variavel}')
print(f'{variavel:z>10}') # Quero que sejam 10 caracteres no total, somando com os inclusos na variável, que no caso são quatro, ou seja, vão ter 6 letras z na ESQUERDA
print(f'{variavel:x<15}') # Quero que sejam 15 caracteres no total, somando com os inclusos na variável, que no caso são quatro, ou seja, vão ter 16 letras x na DIREITA
print(f'{variavel:q^16}') # Quero que sejam 16 caracteres no total, somando com os inclusos na variável, que no caso são quatro, e CENTRALIZE os caracteres da variável

print(f'{3341020.3489727:,.2f}') # Separar a casa de milhar com vírgila (estética) >> Colocando apenas dois números flutuantes
print(f'{1020.3489727:,}') # Separar a casa de milhar com vírgila (estética) >> Deixando todos números flutuantes
print(f'{1020.3489727}') # Deixando o número sem alterações

# Basta por a vírgula depois de ( : ) que irá separar a casa de milhar, ou demais casas por exemplo milhão, bilhão etc.