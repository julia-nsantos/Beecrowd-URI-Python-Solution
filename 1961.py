P, N = [int(x) for x in input().split()] 
if 1 <= P <= 5 and 2 <= N <= 100:
    alturas = [int(x) for x in input().split()]
    resultado = 'YOU WIN'
    for i in range(N-1):
        if abs(alturas[i] - alturas[i+1]) > P:
            resultado = 'GAME OVER'
    print(resultado)   
