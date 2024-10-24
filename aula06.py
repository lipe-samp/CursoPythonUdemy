# Transformando um tipo de variável em outra

print(int("1") + 3) # Transformei a string "1" em número inteiro para poder somar
print(float("14.4") - 4.4) # Transformei a string "14.4" em float e consegui fazer a subtração

print(type(float("7.4")), type(4.4), type(4)) # Observar no terminal que a string "7.4" se converteu em float

print(type(float("7.4") + 5)) # Observar no terminal que vai resultar o tipo de variável como float

print(bool("")) # Transformei uma string em booleana, como não há nada o resultado é False
print(bool(" ")) # Transformei uma string em booleana, basta um caractere para resultar True, nesse exemplo foi o espaço

print(bool("4"), bool("abc"), bool("4.5"), bool("")) 
# Observar no terminal que a única string vazia se converteu em bool False, pois não há nada dentro dela, o restante converteu em True

print(str(11) + "B") # Nesse exemplo transformei a variável int em string (srt) para poder concatenar