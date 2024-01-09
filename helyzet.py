
def gepek_szama(lista):
    db: int= 0
    for i in range(0, len(lista), 1):
        db += lista[i].id
    return db

def atlag(lista):
    paros= 0
    db= 0
    for i in range(0, len(lista), 1):
        if lista[i].hely % 2 == 0:
            paros += i
            db += 1
    return paros/db
    