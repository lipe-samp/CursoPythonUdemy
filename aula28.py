# Exercício:

# Usuário deve digitar o NOME e IDADE
# Se ambos forem digitados deve exibir:
    
    # Seu nome é:
    # Seu nome invertido é:
    # Contém espaços, ou seja, seu nome é composto, ou preencheu sobrenome?
    # Seu nome tem X letras.
    # A primeira letra do seu nome é: 
    # A última letra do seu nome é:

# Se deixar algum campo vazio deve exibir: "Desculpa, você deixou algum campo vazio"

nome = input('Por gentileza, digite seu nome: ')
idade = input('Agora digite sua idade: ')

if nome or idade: # Caso deixe um campo vazio será considerado False, e irá direto para o else
    print(f'Seu nomé é "{nome}".')
    
    if ' ' in nome: # Precisei criar um outro IF para saber se há espaços ou não no nome:
        print('Seu nome contém espaços.')
    else:
        print('Seu nome não contém espaços.')
    
    print(f'Seu nome invertido é "{nome[::-1]}".')
    print(f'Sua idade invertida é "{idade[::-1]}".')
    print(f'Seu nome tem "{len(nome)}" letras.')
    print(f'A primeira letra do seu nome é "{nome[0]}".') # O zero sempre representa o primeiro caractere da string
    print(f'A última letra do seu nome é "{nome[-1]}".') # O negativo conta de trás pra frente, então o -1 vai ser o último caractere da string

else:
    print('Desculpe, você deixou algum campo vazio.')