""" EXERCÍCIO

Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input("Digite um número inteiro: ")

try:
    numero_inteiro = int(numero)
    if numero_inteiro % 2 == 0: # Perguntar se o restante da divisão é igual a 0, pois dessa forma é par
        print("Seu número é par")
    else:
        print("Seu número é ímpar")
except:
    print("Você não digitou um número inteiro")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
print("***********************")

hora = input("Digite o horário atual, sem incluir os minutos: ")

try:
    hora_inteira = int(hora)
    if hora_inteira <= 5:
        print("Madrugada")
    elif hora_inteira <= 11:
        print("Manhã")
    elif hora_inteira <= 17:
        print("Tarde")
    elif hora_inteira <= 23:
        print("Noite")
    else:
        print("Horário inexistente")
except:
    print("Digite um horário em formato de 12h // 00h")


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 5 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 6 e 8 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
print("***********************")

nome = input("Digite seu primeiro nome: ")
if ' ' not in nome:
    if len(nome) <= 5:
        print("Seu nome é curto, com 5 letras ou menos")
    elif len(nome) <= 8:
        print("Seu nome é médio, entre 6 e 8 letras")
    elif len(nome) <= 0:
        print("Você não preencheu o campo necessário")
    else:
        print("Seu nome é grande, com 9 letras ou mais")
else:
    print("Você incluiu espaços, por gentileza somente o primeiro nome.")