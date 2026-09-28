# hello.py
# tu je chybka

import sys

def main():
    print("Zadaj meno!")
    name = input()

    if not name:
        print("Invalid name")
        sys.exit()


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

    if not vek:
        print("Invalid age")
        sys.exit()

    print(f"Mas {vek} rokov")


if __name__ == "__main__":
    main()