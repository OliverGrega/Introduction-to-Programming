slovo = input("Zadaj slovicko: ")

print("Pocet pismen: " + str(len(slovo)))
print("Prve pismeno: " + slovo[0])
print("Posledne pismeno: " + slovo[len(slovo)-1])
print("Slovo povelky: " + str.upper(slovo))
print("Slovo pospat: " + slovo[::-1])

if(slovo == slovo[::-1]):
    print("SLOVO JE DOKONCA AJ PALINDROM")
else:
    print("TOTO SLOVO FAKT NIEJE PALINDROM")    
