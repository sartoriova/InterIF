def desvenda (texto, dic):
    for letra in texto:
        for chave in dic:
            if (letra == chave):
                print( dic[chave], end=" ")

#programa principal

binarios = {"A":"AAAAA", "B":"AAAAB", "C":"AAABA", "D":"AAABB", "E":"AABAA",\
            "F":"AABAB", "G":"AABBA", "H":"AABBB", "I":"ABAAA", "J":"ABAAB",\
            "K":"ABABA", "L":"ABABB", "M":"ABBAA", "N":"ABBAB", "O":"ABBBA",\
            "P":"ABBBB", "Q":"BAAAA", "R":"BAAAB", "S":"BAABA", "T":"BAABB",\
            "U":"BABAA", "V":"BABAB", "W":"BABBA", "X":"BABBB", "Y":"BBAAA",\
            "Z":"BBAAB"}

mensagem = input().upper()

print()
desvenda(mensagem, binarios)
