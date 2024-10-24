# Flag (bandeira) - Marcar um local
# None = "Não valor"
# "is" e "is not" = é ou não é (tipo, valor, identidade)
# id = Identidade 

variavel1 = "a"

print(id(variavel1)) # Ao fazer o print da ID da variável, é possível ver um código no terminal, que significa o valor da memória

variavel2 = "a"

print(id(variavel2)) # Como eu fiz duas variáveis com mesmo valor, o Python armazena o mesmo valor da memória

#_____________________________________________________________________________________________________________________________________________________

condicao = True
variavel = None

if condicao:
    variavel = True
    print("Faça algo")
else:
    print("Não faça algo")

if variavel is True:
    print("Variável passou pelo IF, ou seja, a variável 'condicao 'é True")
else:
    print("Variável não passou pelo IF, ou seja, a variável 'condicao' é False")