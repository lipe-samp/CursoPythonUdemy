adicao = 10 + 10
print ("Adição", adicao)

subtracao = 10 - 5
print("Subtração", subtracao)

multiplicacao = 10 * 10
print("Multiplicação", multiplicacao)

divisao = 10 / 2.2  
# Sempre vai dar resultado como float
print("Divisão", divisao)

divisao_inteira = 10 // 2.2
# O resultado vem como int, se for float aparece o número 0 após a vírgula
print("Divisão inteira", divisao_inteira)

exponenciacao = 2 ** 10
print("Exponenciação", exponenciacao)

modulo = 55 % 2 # O resto da divisão
print("Módulo", modulo)

# Exemplo banaca que usar o módulo, saber se um número é divisível pelo outro
print(10 % 2 == 0) # Como eu sei que 10 é divisível por 2, e resta 0, retorna True
print(11 % 2 == 0) # Agora eu seu que não é divisível, vai retornar como False