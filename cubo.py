N = int(input(""))

cubos = N ** 3
uma = (((N-2)**2)*6)
duas = ((N-2)*12)
nenhuma = cubos - (uma + duas + 8)

print(nenhuma)

print(uma)

print(duas)

print("8")
