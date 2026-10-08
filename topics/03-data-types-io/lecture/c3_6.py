txt = input("Zadaj slovo: ")

for s in txt[::]:
    u = ord(s)
    b = s.encode("utf-8")

    print(f"{s} U+{u:04X} {len(b)} B")