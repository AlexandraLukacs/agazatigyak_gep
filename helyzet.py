from Gepek import Gepek

fajlom = open("gep.txt", "r", encoding='utf-8')
fajlom.readline()
lista=fajlom.readlines()
fajlom.close()

def gepel_szama():
    for i in range(0, len(lista), 1):
        i += 1
    print(f"A gépek száma: {i}")

def atlag():
    for i in range(0, len(lista), 1):
        