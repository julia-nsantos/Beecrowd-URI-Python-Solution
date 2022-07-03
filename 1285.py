while True:
    try:
        n, m = input().split()
        contagem = 0

        for i in range(int(n),int(m)+1):
            if(len(set(list(str(i)))) == len(str(i))):
                contagem += 1
        print(contagem)
        
    except EOFError:
        break
