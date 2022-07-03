x,y = map(int, input().split())

resto = max(x,y)%min(x,y)

if resto == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
