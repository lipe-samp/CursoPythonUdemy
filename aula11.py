# Precedência dos operadores aritiméticos

# 1º (n + n)
# 2º **
# 3º * / // %
# 4º + -

conta_1 = 1 + 1 ** 5 + 5 
print(conta_1)

conta_2 = (1 + 1) ** (5 + 5) 
print(conta_2)

conta_3 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_3)