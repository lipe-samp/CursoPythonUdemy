# Ainda sobre if / elif / else
condicao_1 = False
condicao_2 = True
condicao_3 = True
condicao_4 = False

if condicao_1:                                          # Somente posso colocar um "if"
    print('Cóigo para condição 1')

elif condicao_2:                                        # Posso colocar quantos "elif" eu quiser
    print('Código para condução 2')                     

elif condicao_3:                                        # Posso colocar quantos "elif" eu quiser
    print('Código para condição 3')

elif condicao_4:                                        # Posso colocar quantos "elif" eu quiser
    print('Código para condição 4')

else:                                                   # Somente posso colocar um "else"
    print('Nenhuma condição foi satisfeita')

# Só vai imprimir no terminal a variável booleana com valor "True"
# Se houver mais de uma variável com valor "True", somente a primeira será executada no terminal, em sua respectiva ordem
