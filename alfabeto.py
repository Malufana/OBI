entrada = input("")
K, N = map(int, entrada.split())

P = input("")
M = input("")

alfabeto = list(P)
mensagem = list(M)
aux = False

if len(M) == N and len(P) == K:
    for i in alfabeto:
        for j in mensagem:
            if j in alfabeto:
                aux = True
            else:
                aux = False
                break
    if aux == True:
        print("S")
    else:
        print("N")             
           
