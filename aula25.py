# Interpolação básica de strings >> é estilo f-strings, exemplo: (f'Ola meu nome é {variavel}')

# %s - string
# %d ou %i - int
# $f - float
# %x ou %X - Hexadcimal, que são (ABCDEF0123456789)


nome = 'Felipe' # Essa variável é uma string, sendo assim (%s)
preco = 120.777  # Essa variável é um float, sendo assim (%f), ou (%.2f) caso eu queira reforçar que são somente 2 números após a vigula

variavel = 'Tudo bem, %s? O preço é %f, arredondando para %.2f' % (nome, preco, preco) # Interpolação é esse conjunto de strings, mas é um jeito mais complexo

# Basta colocar % após o valor da variável, a que está rosa, e todas as demais variáveis dentro de ()
print(variavel)
#________________________________________________________________________________________________________________________
print('O Hexadecimal de %i é %X ou %08X' % (401055000000000000, 401055000000000000, 401055000000000000)) 
# Coloquei 08 antes do X para que sejam no mínimo 8 caracteres, e se não houver coloque o 0
# Hexadecimal %x ou %X deve ser em formato de número INTEIRO, se for string ou float irá quebrar