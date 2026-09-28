# hello.py
def main():
    print("Zadaj meno!")
    name = input()
    print("Chces formalny pozdrav? [Y/N]")
    choice = input()
    if(choice == 'N'):
        print(f"Čus, {name}")
    elif(choice == 'Y'):
        print(f"Dobre jitro, pane {name}")
    else:
        print("TAK TOHLE FAKT NE CHLAPE")

    print("Zadaj vek!")
    vek = input()
    print(f"Mas {vek} rokov")


if __name__ == "__main__":
    main()