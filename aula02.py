# Entendendo a função print(), é usada para exibir (printar) algo na tela

print(12, 34, sep="x") # O comando > sep="" < define como serão separados os itens dentro de print
print(12, 34, end="\r\n") # O comando > end="\r\n" ou somente \n < significa a quebra de linha
print(12, 34, end="@") # Nesse exemplo eu troquei a quebra de texto, que já é automática, por um > @ <
print(12, 34)
print(12, 34, end="@@\n") # Nesse caso eu coloquei duas ações ao mesmo tempo, finalizar com > @ < e quebrar a linha
print(12, 34)
print(12, 34, end="\n@@") # Nesse caso eu coloquei primeiro a quebra de linha, sendo assim o > @ < foi para a linha de baixo
print(12, 34, sep="XXX") # Reforçar a função separadora