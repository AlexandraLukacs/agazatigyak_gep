import random

lista = []

def tizzeloszthatoszam():
    print("2. Feladat")
    for i in range(15):
        szam: int= random.randint(-90, 500)
        lista.append(szam)
        if i < 14:
            print(szam, end = "* ")
        else:
            print(szam, end = " ")

def oszthatoak_szama():
    db: int= 0
    for i in range(0, len(lista), 1):
        if lista[i] % 10 == 0:
            db += 1
        i += 1
    return db