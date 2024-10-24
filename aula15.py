# Como coletar dados dos usuários

nome = input('Qual o seu nome? ')

print(f'Seu nome é {nome}')

idade = input('Digite sua idade: ') # o input sempre recebe valor de string 
multiplicar = input('Multiplique por algum número: ') 

int_idade = int(idade) 
int_multiplicar = int(multiplicar)
# Criei duas novas variáveis apenas trocar o valor de string para int, 
# Eu poderia fazer na variável primária, porém assim eu posso saber onde o usuário errou, que ao invés dele digitar número, digitou letra

resultado = int_idade * int_multiplicar

print(f'Sua idade, {int_idade}, multiplicada por {int_multiplicar} é igual a {resultado}')