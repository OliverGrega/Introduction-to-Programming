x = input("Zadaj slovo: ")

print(f"Veta {x}")

newDict = { }

x = x.lower()
for p in x[::]:
    if(p.isalpha()):
        if p in newDict:
            newDict.update({p : newDict[p]+1})
        else:
            newDict[p] = 1

for x, y in newDict.items():
    print(f"{x}: {y}")

print(f"Roznych pismen: {len(newDict)}")