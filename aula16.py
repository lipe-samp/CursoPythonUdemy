# Operações condicionais

# if / elif      / else
# se / se não se / se não

nome_usuario = input('Qual o seu nome, por gentileza? ')

pergunta = input(f'{nome_usuario}, você deseja comprar este produto? ')

if pergunta == 'sim':
    print(f'Parabéns {nome_usuario}, compra realizada com sucesso.')
    print('Obrigado pela preferência!')

elif pergunta == 'não':
    print('Você cancelou a compra.')
    print('Estamos à disposição para atender qualquer dúvida.')

else:
    print(f'Perdão {nome_usuario}, não entendi o que quis dizer, responda apenas com "sim" ou "não".')

# Diferente do html, preciso que tenha o espaço na próxima linha para ficar dentro do bloco if / elif / else
# Se não houver o espaço, não vai estar em nenhuma condição, como no exemplo a seguir:

print('Não estou em nenhuma condição, sempre irei aparecer')