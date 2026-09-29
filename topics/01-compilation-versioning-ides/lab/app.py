# hello.py
# tu je chybka

import sys

def main():
    print("Zadaj meno!")
    name = input()

    if not name:
        print("Invalid name")
        sys.exit()

    #checkne ci bude pozdrav formal
    print("Chces formalny pozdrav? [Y/N]")
    choice = input()
    if(choice == 'N'):
        print(f"Čus, {name}")
    elif(choice == 'Y'):
        print(f"Dobre jitro, pane {name}")
    else:
        sys.exit()


    print("Chces pozdrav v uppercasu? [Y/N]")
    #nacita ci ma byt pozdrav uppercasu
    upper = input()
    if(upper == 'Y'):
        output = output.upper()

    print(output)

    print("Zadaj vek!")
    #Nacita vek
    vek = input()

    #skontroluje ci je input veku validny
    if not vek:
        print("Invalid age")
        sys.exit()

    print(f"Mas {vek} rokov")


if __name__ == "__main__":
    main()