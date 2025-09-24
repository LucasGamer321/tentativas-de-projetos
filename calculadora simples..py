print("Escolha o operador:\n"
      "[1] +\n"
      "[2] -\n"
      "[3] *\n"
      "[4] /\n"
      "[5] sair do programa\n")
escolha = str(input("escolha o operador: ")).strip()
while escolha != 5:
    numero = float(input("digite um numero: "))
    numero2 = float(input("digite outro numero: "))
    if escolha == 1:
        print(numero + numero2)
    elif escolha == 2:
        print(numero - numero2)
    elif escolha == 3:
        print(numero * numero2)
    elif escolha == 4:
        print(numero / numero2)
    pergunta = str(input("Quer continuar? [S/N] ")).upper().strip()
    if pergunta in "Nn":
        break
print("fim")






