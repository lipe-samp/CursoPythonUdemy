# Introdução ao try / except

# try (Tentar executar um código)
# except (Ocorreu um erro ao executar)

numero_str = input("Digite um número para duplicar: ")

try:
    print(f"Você digitou: {numero_str}")
    numero_int = int(numero_str) # Similar ao IF ELSE, porém vai ler todo o TRY, se encontrar algum erro vai pular direto para o EXCEPT
    print(f"O dobro de {numero_int} é {numero_int * 2}")
except:
    print("Não digitou um número") # Se não houver nenhum erro no TRY, o EXCEPT não vai ser executado

# TRY vai ler até a linha que houver um erro, se o erro for na primeira linha, vai ignorar e ir direto para o EXCEPT