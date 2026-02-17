nome = input("Qual seu nome completo:")
idd = input("Qual sua idade:")
if nome and idd:
    print( f"seu nome é {nome}")
    print(f"Sua idd é {idd}")
    print(f'seu nome invertido é {nome[::-1]}')
    print(f'seu nome tem {len(nome)} letras')
    print(f'a ultima letra do seu nome é {nome[-1]}')
    print(f'a primeira letra do seu nome é {nome[0]}')

    if ' ' in nome:
            print("seu nome tem espaços")
    else:
        print("seu nome não tem espaços")
else:
    print("digite algo")