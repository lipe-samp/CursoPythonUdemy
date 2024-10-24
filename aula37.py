'''
Repetições
while (enquanto)
Executa enquanto ação for verdadeira
Loop infinito, não tem fim.
'''

contador = 0 # Coloquei zero pois que quero que contador inicie do zero

while contador <= 100:
    contador += 1

    if contador == 15:
        continue # o Continue faz retormar para o while, ou seja, não executou o print abaixo

    if contador >= 20 and contador <= 27:
        continue
        # Vai pular todos os números de 20 até 27

    print(contador) # Vai printar todos os números menos o (15) e (20 até 27)

    if contador == 50:
        break # Finalizei no 50, mesmo colocando 100 no while
