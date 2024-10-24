# Operadores lógicos >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> (and) (or) (not)

# Vamos falar somente sobre (and)

# (and) Todas as condições precisam ser True
# (and) Se uma condição for False, a expressão inteira será considerada False
# (and) O valor False irá sobrepor qualquer True que houver na expressão, mesmo se for somente um

# São considerados False: 0 (zero) 0.0 (zero vírgula zero) '' (string vazia) False (a própria palavra False)

# Existe o valor None, um valor vazio (não valor), mas não é o mesmo que False

print('Cadastre-se:')
print('')
login = input('Crie seu usuário: ')
senha = input('Crie sua senha: ')
print('')
print('Agora vamos tentar fazer login')
print('')
login_salvo = input('Usuário: ')
senha_salva = input('Senha: ')
print('')
if login_salvo == login and senha_salva == senha:
    print('Bem vindo ao sistema!')
else:
    print('Usuário ou senha incorretos.')

# O False recebe o valor da expressão:
print(True and True and True and False and True) # Vai ser impresso somente o False