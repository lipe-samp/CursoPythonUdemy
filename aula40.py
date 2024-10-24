# Calculadora com while

""" Calculadora com while """
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    num_1_float = 0
    num_2_float = 0

    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print("De acordo com seus dados, segue a conta abaixo: ")

    if operador == "+":
        print(f"{num_1_float} + {num_2_float} = {num_1_float + num_2_float}")
    elif operador == "-":
        print(f"{num_1_float} - {num_2_float} = {num_1_float - num_2_float}")
    elif operador == "*":
        print(f"{num_1_float} * {num_2_float} = {num_1_float * num_2_float}")
    elif operador == "/":
        print(f"{num_1_float} / {num_2_float} = {num_1_float / num_2_float}")

    ###

    sair = input('Quer sair? [s]im: ').lower().startswith('s') # transformando a string em booleana como True, caso comece com s

    if sair is True: 
        break