# Outra forma de formatar strings
a = 'AAA'
b = 'BBB'
c = 1.1554

texto = 'a = {} b = {} c = {:.2f}' # Apenas criando string, lembrando que > :.2f < é para dizer a quatidade de números após vírgula
formatado = texto.format(a, b, c)
print(formatado)

# Usando o .format() é semelhante a aula anterior, que eu coloquei > f < antes da string
# Na variável > texto < eu criei uma string e quero que as variáveis > a, b, c < apareçam
# A ordem que irão aparecer vai depender de como eu coloquei dentro do .format()

texto_2 = 'c = {2:.2f} a = {0} a = {0} a = {0} b = {1}' # Apenas criando string
formatado2 = texto_2.format(a, b, c) 

print(formatado2)

# Agora eu que escolhi qual a ordem que irá aparecer nos {}
# No .format() a ordem das variáveis são 0,1,2,3...
# Sendo assim eu escolhi {2} {0} {0} {0} {1}, ou seja, eu consigo repetir

texto_3 = 'a = {nome1} b = {nome2} c = {nome3:.2f}' # Apenas criando a string
formatado3 = texto_3.format(
    nome1 = a, nome2 = b, nome3 = c
) 

print(formatado3)

# Nesse exemplo acima, ao invés de usar {0} {1} {2},
# Ou seja, eu posso nomear cada variável dentro do .format() para facilitar na hora de colocar na string