L = int(input())
T = input().upper()
soma, media = 0, 0
matriz = list()
for i in range (12):
    matriz.append(list(range(12)))

for linha in range(12):
    for coluna in range(12):
        matriz[linha][coluna] = float(input())
        
for coluna in range(12):
        soma += matriz[L][coluna]
if T == 'S':
    print(f'{soma:.1f}')
elif T == 'M':
    media = soma/12
    print(f'{media:.1f}')
