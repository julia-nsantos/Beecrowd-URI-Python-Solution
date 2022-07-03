soma = 0
quantidade = 0

while True:
    idade = int(input())
    if idade < 0:
        break
    else:
        soma += idade
        quantidade += 1

print(f"{soma/quantidade:.2f}")
