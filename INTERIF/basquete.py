def basquete(int1, int2):
    porcentagem = (int2/int1)*100
    print("%.2f" %porcentagem, end="")
    print("%")

#programa principal

arremessei = int(input())
acertei = int(input())

basquete(arremessei, acertei)
