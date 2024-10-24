# Testando o DEBUG do código da aula  anterior

condicao_1 = False     # Observar que eu maquei a "bolinha vermelha" nessa linha, pois irei executar linha por linha no DEBUG
condicao_2 = True
condicao_3 = True
condicao_4 = False

if condicao_1:                                          
    print('Cóigo para condição 1')

elif condicao_2:                                       
    print('Código para condução 2')       # Como o Debug encontrou esse valor como True, ele automaticamente vai pular as demais condições              

elif condicao_3:                                       
    print('Código para condição 3')

elif condicao_4:                                       
    print('Código para condição 4')

else:                                                   
    print('Nenhuma condição foi satisfeita')

if (10 == 10):
    print('Após debugar e encontrar o valor True, o código avança diretamente aqui') # Top demais