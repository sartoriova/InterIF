import math

def figurinhas (real, lista):
    tenho = 0.25*lista[0] + 0.10*lista[1] + 0.05*lista[2] + 0.01*lista[3]
    compro = tenho/real
    print ( math.floor(compro) )

    qtd_moedas = lista[0] + lista[1] + lista[2] + lista[3]
    sobrou = tenho - real
    print( math.floor(qtd_moedas*sobrou) )
#programa principal

custa = input()
qtd = input()

novo_custa = float( custa[2:] )

lista = qtd.split()

lista_qtd = []

for numero in lista:
    lista_qtd.append( int(numero) )
    
figurinhas(novo_custa, lista_qtd)
