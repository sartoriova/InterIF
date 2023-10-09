import math

def vezes_completo (int1, int2, int3):
    km = int1/1000
    
    resultado = math.floor( (int2*int3)/km )

    return resultado

#programa principal

dados = input()

lista = dados.split()
nova_lista = []

for numero in lista:
    nova_lista.append( int(numero) )

metros = nova_lista[0]
kmh = nova_lista[1]
horas = nova_lista[2]

print( vezes_completo(metros, kmh, horas) )

