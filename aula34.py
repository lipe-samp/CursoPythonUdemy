# Condição while (enquanto)

condicao = True

while condicao:
    permanecer_rodando = input("Digite qualquer coisa para permanecer. Digite '0' ou 'sair' para sair. ")
    print(f"Você digitou {permanecer_rodando}.")

    if permanecer_rodando == "sair" or permanecer_rodando == "0":
        print("Fim do loop.")
        break
