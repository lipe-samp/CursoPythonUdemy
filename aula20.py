# Exercício
# Criar dois input e comparar se um valor é maior que o outro

numero_1 = input('Digite o primeiro valor: ')
numero_2 = input('Digite o segundo valor: ')

if numero_1 > numero_2:
    print(f'O primeiro valor "{numero_1}" é maior do que o segundo valor "{numero_2}"')
elif numero_1 < numero_2:
    print(f'O primeiro valor "{numero_1}" é menor do que o segundo valor "{numero_2}"')
elif numero_1 == numero_2:
    print(f'Os valores "{numero_1}" e "{numero_2}" são iguais')
else:
    print("Você realmente digitou o número correto?")