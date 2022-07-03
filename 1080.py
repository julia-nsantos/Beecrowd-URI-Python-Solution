posicao = 0
maior = 0
for i in range(1,101):
    N=int(input())
    if(N>=maior):
        maior=N
        posicao=i
print(maior)
print(posicao)
