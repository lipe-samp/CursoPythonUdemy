"""
Iterando strings com while
"""

nome = "Felipe Sampaio"

posicao = 0  # A posição da letra, sempre a primeira posição é 0
# "F" vale 0, "e" vale 1, "l" vale 2, "i" vale 3 ...

novo_nome = "" # Deixar em branco pois vai entrar letra por letra

# Enquanto posição da letra for menor que a quantidade máxima de posições da variável nome (14 caracteres)
while posicao < len(nome):

    letra = nome[posicao] 
    # Variavel letra vai pegar a posição, se for 0 vale "F", se for 1 vale "e"
    # (letra por letra, uma de cada vez, pois o indice vai aumentar)

    novo_nome = novo_nome + letra 
    # Agora vamos criar um nome completo pegando a letra da variável letra e colocando asterísco depois dela
    
    posicao = posicao + 1 
    # Somamos a posicao pois agora vai valer 1, ou seja, segunda letra do nome, depois terceira, até a última

print(novo_nome)