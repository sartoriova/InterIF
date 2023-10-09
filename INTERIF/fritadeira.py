def converte_graus (numero):
    resultado = int( ((numero*9)/5)+32 )
    return f"{numero} graus celsius equivale a {resultado} graus fahrenheit"

#programa principal

celsius = int( input() )

print( converte_graus(celsius) )
