r = 0
e = 0

while e == 0:
    num = int(input("Qual o primeiro numero: "))
    num2 = int(input("Qual o segundo numero: "))
    p = input("Qual operação você quer (+, -, *, /)? ").lower().strip()

    if p == "soma" or p == "+":
        r = num + num2
    elif p == "subtração" or p == "-":
        r = num - num2
    elif p == "divisão" or p == "/":
        if num2 != 0: 
            r = num / num2
        else:
            print("Erro: Não é possível dividir por zero!")
    elif p == "multiplicação" or p == "*":
        r = num * num2
    else:
        print("Operação inválida!")
        continue

    print(f'O resultado foi {r}')
    
    menu = input("Quer continuar [S/N]? ").lower().strip()
    
    if menu == "n":
        e += 1
        print("Encerrando...")
    else:
        print("Vamos continuar!\n")