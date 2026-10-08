sec = int(input("Zadaj sekundy"))

min = sec // 60

hod = min // 60

sec = sec % 60
min = min % 60

print(f"{hod}:{min}:{sec}")
