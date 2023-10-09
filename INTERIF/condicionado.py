def ajusta_ar (palavra, dic):
    for chave in dic:
        if (palavra == dic[chave]):
            confere = True
            return chave
    confere = False
    if (not confere):
        return "COMANDO INVALIDO"

#programa principal

opcoes_ar = {24:"FRIO", 20:"MUITO FRIO", 18:"EXTREMAMENTE FRIO", 28:"QUENTE"}

ar = input().upper()

print( ajusta_ar (ar, opcoes_ar) )
        
        
