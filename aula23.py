# Operadores lógicos >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> (and) (or) (not)

# Vamos falar somente sobre (not)

# É usado para inverter expressões
# not True = False
# not False = True

senha = input('Digite sua senha: ') # Deixa em branco é igual a False
if not senha: # Porém o (not) inverteu para True e imprimiu no terminal 
    print('Você não digitou nada')
elif senha == '123456':
    print('Senha correta')
else:
    print('Senha inválida')