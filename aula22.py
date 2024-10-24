# Operadores lógicos >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> (and) (or) (not)

# Vamos falar somente sobre (or)

# (or) Basta uma condição ser True para toda expressão ser considerada True

usuario = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')

if usuario == 'admin1' or usuario == 'admin2' and (senha == '123456' or senha == 'abcdef'): 
    print('Login realizado com sucesso!')
else:
    print('Usuário ou senha incorretos.')

# Usei a lógica or para que que se pelo menos uma condição for True, eu consiga continuar a executar o código
# Criei 2 resultados possíveis para cada variável