def quem_ganhou (nmr1, nmr2):
    r = (3*nmr1)**2 + nmr2**2 
    b = 2*(nmr1**2) + (5*nmr2)**2 
    c = -100*nmr1 + nmr2**3 
    if (r > b) and (r > c):
        return "Rafael ganhou"
    elif (r < b) and (c < b):
        return "Beto ganhou"
    elif (r < c) and (b < c):
        return "Carlos ganhou"

#programa principal

x = int(input())

y = int(input())

print( quem_ganhou(x, y) )
