entrada = input("")
Ai = input("")
N, K = map(int, entrada.split())
A1 = list(map(int, Ai.split()))

A1.sort(reverse=True)

print(A1[K-1])


