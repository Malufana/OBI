placa = input("").upper()

tamanhoPlaca = len(placa)

if tamanhoPlaca == 7 and placa[0:2].isalpha() and placa[3].isdecimal() and placa[4].isalpha() and placa[5:6].isdecimal():
    # if placa[0:2].isalpha() and placa[3].isdecimal() and placa[4].isalpha() and placa[5:6].isdecimal():
    print("2")
elif tamanhoPlaca == 8 and placa[0:2].isalpha() and placa[3] == "-" and placa[4:7].isdecimal:
    # if placa[0:2].isalpha() and placa[3] == "-" and placa[4:7].isdecimal:
    print("1")
else:
    print("0")
