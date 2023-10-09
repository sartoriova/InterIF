def multiplos (string):
    lista_par = []
    lista_impar = []
    
    for numero in string:
        if ( int(numero) % 2 == 0):
            lista_par.append( int(numero) )
        else:
            lista_impar.append( int(numero) )
            
    soma_par = sum(lista_par)
    soma_impar = sum(lista_impar)

    if (soma_par % 3 == 0):
        print("S")
    else:
        print("N")

    if (soma_impar % 3 == 0):
        print("S")
    else:
        print("N")

#programa principal

numero = int( input() )

novo_numero = str(numero)

multiplos(novo_numero)

