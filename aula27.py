# Fatiamento de string

#  012345678 >>> Positivo começa do zero
#  Olá mundo
# -9-8-7-6-5-4-3-2-1 >>> Negativa começa do menos um (de trás pra frente)

# Fatiamento [i:f:p] [::] >>> i (inicio) f (fim)

variavel = 'Olá mundo'

print(variavel[2:7]) # Fatiei a string com o inicio o caractere 2 e finalizando com caractere 7 

# IMPORTANTE PARA NÃO CONFUNDIR: A string sempre começa com 0, sendo assim a sétima letra no caso é a sexta

# Se eu quiser que preencha até o final eu deixo o f em branco >> [i:f:p]
# Exemplo a seguir:
print(variavel[2:]) # Iniciei do caractere 2 (terceira letra pois começa com zero), e deixei ir até o fim pois não especifiquei depois do : onde eu quero que termine essa fatia 

print(variavel[:6]) # Finalizei com caractere 6 
# Finalizar parece um pouco confuso, pois normalmente o último é omitido, sendo assim o último que vai aparecer neste caso é o 5
# No caso de finalizar sempre pense em colocar uma unidade a mais
# Pra facilitar, quando eu não especifico o começo ele realmente printa 6 caracteres, diferente de quando eu pego do inicio, que o zero é contado

print(variavel[1:6]) 
# Agora um exemplo escolhendo o início e o fim da minha fatia, lembrando que o primiro caracteze é zero, por isso printou "lá mu" de "Olá mundo"
# E o último não aparece, se eu pedi para terminar no [6] o último a ser printado foi o [5]

# Função len() serve para contar quantos caracteres tem na string, porém não começa do zero igual no fatiamento
print(len(variavel)) # 'Olá mundo' tem 9 caracteres, então irá printar 9
# O len() também significa o fim da  variável, se eu quiser fatiar e não sei quantos caracteres tem na string, eu posso usar o len()

# Exemplo a seguir:
print(variavel[0:len(variavel):1]) # DETALHE: Agora estou usando o terceiro número de [i:f:p], que seria o p (passo)
# É simples, o padrão é 1, que imprime todos caracteres, se eu colocasse 2, ele iria printar de dois em dois caracteres.

# Exemplo de 2 em 2:
print(variavel[0:len(variavel):2]) # Eu poderia trocar o len(variavel por 9, não tem problema, pois eu sei quantos caracteres tem)
print(variavel[0:9:2]) # Mesma coisa nos dois casos

# INTERESSANTE: eu posso fazer a impressão de trás pra frente, usando os dados com números negativos
print(variavel[::-1]) # Deixando em branco para pegar todos
print(variavel[-1:-10:-1]) # Ou escolhendo a fatia que eu quero de trás pra frente
# Nesse exemplo eu quis aparecer todos, então coloquei uma unidade negativa a mais no fim, que no caso era -9 e ficou -10
# Lembrar que sempre coloca uma unidade a mais do que eu quero que apareça