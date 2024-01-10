from Gepek import Gepek

gepek_lista=[]
fajlom = open("gep.txt", "r", encoding='utf-8')
fajlom.readline()
lista=fajlom.readlines()
fajlom.close()
for i in range(0, len(lista), 1):
    aktsor:str=lista[i].strip()
    print(aktsor)
    sor_lista=aktsor.split("!")
    print(sor_lista[0])
    print(sor_lista[1])
    print(sor_lista[2])
    print(sor_lista[3])
    gepek=Gepek(int(sor_lista[0]), sor_lista[1], sor_lista[2], sor_lista[3])
    gepek_lista.append(gepek)

for i in range(0, len(gepek_lista), 1):
    print(f"{gepek_lista[i].id}, {gepek_lista[i].hely}, {gepek_lista[i].tipus}, {gepek_lista[i].ipcim}")

import helyzet

def szama():
    db=helyzet.gepek_szama(gepek_lista)
    print(f"A gépek száma: {len(lista)}")

def atlag_szam():
    atlaga=helyzet.atlag(gepek_lista)
    print(f"Átlag: {atlaga}")