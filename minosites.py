def museum_feladat1():
    print("1. Feladat")
    museum_nev: str= str(input("Múzeum neve: "))
    latogato_nev: str= str(input("Látogató neve: "))
    ertekeles: int= int(input("Értékelés (1-20): "))
    if ertekeles < 1: 
        print("Az értékelés nem lehet negatív vagy 0!")
    elif ertekeles > 20: 
        print("20 pont feletti értékelés nem elfogadható!")
    else: 
        print("Köszönjük az értékelést!")
