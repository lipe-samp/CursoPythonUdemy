'''
Operadores de atribuição
=    +=    -=    *=    /=   //=   %=
'''

contador = 0 # Coloquei zero pois que quero que contador inicie do zero

while contador <= 10:
    print(contador)
    contador += 1 # Mesma ação que: contador = contador + 1

print("Acabou")

contador = 10

# contador = contador * "t"
contador *= "t" 
# Nesse caso a variavel contador era o número 10, e eu mudei que o contador seja seu antigo valor, 10, multiplicado pela string "t" 

print(contador) # Valor: "tttttttttt"