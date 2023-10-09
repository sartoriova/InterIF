def jokenpo(str1, str2, dic):
    for chave in dic:
        if (str1 == str2):
            return "Empate"
        elif ( (chave == str1) and (dic[chave] == str2) ):
            return "Jogador 2"
        elif ( (chave == str1) and (dic[chave] != str2) ):
            return "Jogador 1"

#programa principal

maiores = {"pedra":"papel", "papel":"tesoura", "tesoura":"pedra"}

jogador1 = input().lower()
jogador2 = input().lower()

print( jokenpo(jogador1, jogador2, maiores) )
