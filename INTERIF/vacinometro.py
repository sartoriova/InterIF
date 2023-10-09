def vacinometro(int1, int2):
    porcentagem = (int2/int1)*100
    print("%.1f" %porcentagem, end="")
    print("%")

#programa principal

habitantes = int(input())
vacinados = int(input())

vacinometro(habitantes, vacinados)
