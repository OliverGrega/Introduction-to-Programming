x = int(input("Zadaj cele nezaporne cislo: "))

if(x > 0):
    b = ""
    kontrola = bin(x)
    while(x > 0):
        if(x % 2 != 0):
            b += "1"
        else:
            b += "0"

        x //= 2
    
    print("Dvojkovo: " + str(b[::-1]))
    print("Kontrola: " + kontrola)
    print("Pocet bitov: " + str(len(b)))

    j = 0
    for i in b[::]:
        if(i == '1'):
            j+=1

    print("Pocet jednotiek: " + str(j))
