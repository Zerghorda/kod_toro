import random

szinek = ["piros", "kék", "zöld", "sárga", "narancs", "lila"]


def gep_tip(szin_lista):
    megoldas = []
    for i in range(4):
        szin = szin_lista[random.randint(0, 5)]
        megoldas.append(szin)
    return megoldas


gep_megoldas = gep_tip(szinek)
print(gep_megoldas)
print("lehetséges színek: piros, kék, zöld, sárga, narancs, lila")


def tipelesek(szin_lista):
    tip_lista = []
    db: int = 0
    while db < 4:
        tip = input("szín:")
        while tip not in szin_lista:
            print("nincs ilyen szín!")
            tip = input("szín:")
        tip_lista.append(tip)
        db += 1

    return tip_lista


jatekos_tip = tipelesek(szinek)


def tip_kiir(jatekos):
    print("tippje: ", end="")
    for i in range(len(jatekos)):
        if i == len(jatekos) - 1:
            print(f"{jatekos[i]}")
        else:
            print(f"{jatekos[i]}", end=",")


tip_kiir(jatekos_tip)


def jatek(gep, jatekos):
    db: int = 0
    gyozot: bool = False
    fekete: int = 0
    feher: int = 0
    while db < 9 and not gyozot:
        for i in range(len(jatekos)):
            if i == gep.index(jatekos[i]):
                fekete += 1
            elif gep.index(jatekos[i]) > -1:
                feher += 1
            else:
                pass
            if fekete == 4:
                gyozot = True
        db += 1
        tipelesek(szinek)
        print(fekete)
        print(feher)
    if gyozot and db <= 9:
        print("Kitaláltad !")
    if db > 9:
        print("Majd legközelebb!")
        print(f"Ez lett volna a válasz: {gep}")



jatek(gep_megoldas, jatekos_tip)
