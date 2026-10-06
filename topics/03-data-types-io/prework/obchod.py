
def main():
    nazovPolozky = str(input("Položka: "))
    cenaPolozky = float(input("Cena za kus [Kč]: "))
    pocet = int(input("Pocet kusov: "))
    
    print(f"{nazovPolozky}: {pocet} x {cenaPolozky} = {(pocet * cenaPolozky):.2f} Kč")


if __name__ == "__main__":
    main()