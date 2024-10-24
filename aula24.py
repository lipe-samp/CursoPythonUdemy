# Operadores (in) "está entre" e (not in) "não está entre"
# Strings são iteráveis > Posso navegar item por item

# A seguir um exemplo de iteravel: (letra por letra)
#  0 1 2 3 4 5
#  F e l i p e
# -6-5-4-3-2-1
#________________________________________________________________________________________________________________________
nome = 'Felipe' # (Observar matriz acima)
print(nome[4])  # Ao colocar o [4], ele imprimiu somente a letra 'p'
print(nome[-6]) # Ao colocar o [-6], ele imprimiu somente a letra 'F'
print(nome[-1]) # Ao colocar o [-1], ele imprimiu somente a letra 'e'
#________________________________________________________________________________________________________________________
# Agora usando (in)
print('F' in nome)   # Ao afirmar se há 'F' na variável 'nome', vai retornar como True
print('ipe' in nome) # Ao afirmar se há 'ipe' na variável 'nome', vai retornar como True, pois há sim essa sequência na string
print('g' in nome)   # Ao afirmar se há 'g' na variável 'nome', vai retornar como False
#________________________________________________________________________________________________________________________
# Agora usando (not in)
print('F' not in nome)   # Ao afirmar que não há 'F' na variável 'nome', vai retornar como False, pois há sim
print('ipe' not in nome) # Ao afirmar que não há 'ipe' na variável 'nome', vai retornar como False, pois há sim
print('g' not in nome)   # Ao afirmar que não há 'g' na variável 'nome', vai retornar como True, pois realmente não há
#________________________________________________________________________________________________________________________
#Brincando
nome_2 = input('Digite seu nome: ')
encontrar = input ('No seu nome há: ') # Digitar letra ou conjunto de letras na sequência que iremos encontrar na variável nome_2

if encontrar in nome_2:
    print(f'Sim, "{encontrar}" está dentro de "{nome_2}".')
else:
    print(f'Não, "{encontrar}" não está dentro de "{nome_2}".')
#________________________________________________________________________________________________________________________
# Exemplo de atividade que posso colocar vários (if) e (else) consecutivos. NÃO HÁ RELAÇÃO com (in) e (not in)
numero = 10
if numero > 1:
    if numero > 2:
        if numero > 3:
            print('Número maior que 3')
        else:
            print('Número menor que 3')
    else:
        print('Número menor que 2')
else:
    print('Número menor que 1')