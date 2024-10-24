nome = 'Felipe Sampaio'
altura = 1.78
peso = 86
imc = peso / (altura * altura)
decimal_grande = 1.78888 # Para testar quantas numeros após a vírgula eu quero que apareça

linha_1 = f'{nome} tem {altura} de altura'
# O fato de colocar o f antes da string permite que eu coloque variáveis juntas, basta usar {}

linha_2 = f'Ele pesa {peso} quilos e seu imc é {imc:.2f}'
# Colocando > :.2f < após a variável float, eu digo quantos números vão aoarecer depois da vírgula


print(linha_1)
print(linha_2)

