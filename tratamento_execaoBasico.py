num_str = input("digite um numero: ")


try:
    print('STR:', num_str)
    num_flot = float(num_str)
    print(f'o dobro de {num_str} é {num_flot * 2:f} ')
except:
    print("digite um num")