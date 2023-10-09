def ajudaNoTruco (nmr, dic):
    for chave in dic:
        if (chave == nmr):
            for indice in range(0,len(dic[chave])):
                print(dic[chave][indice], end=" ")

#programa principal

manualTruco = {1:[2, 3], 2:[3], 3: [0], 4:[5, 6, 7, 11, 12, 13, 1, 2, 3], 5:[6, 7, 11, 12, 13, 1, 2, 3], 6:[7, 11, 12, 13, 1, 2, 3], 7:[11, 12, 13, 1, 2, 3], 11:[12, 13, 1, 2, 3], 12:[13, 1, 2, 3], 13:[1, 2, 3]}

nmrCarta = int(input())

ajudaNoTruco(nmrCarta, manualTruco)

