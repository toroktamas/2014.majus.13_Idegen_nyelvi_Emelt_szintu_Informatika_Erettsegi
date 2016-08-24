#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""2014.majus.13 Idegen nyelvi Emelt szintu erettsegi python programozas."""

def loertek(sor):
    aktpont = 20
    ertek = 0
    for i in range(1, len(sor)):
        if aktpont > 0 and sor[i] == "-":
            aktpont = aktpont-1
        else:
            ertek = ertek+aktpont
    return ertek

#print("1. feladat")
"""Be kell olvasni verseny.txt fajt.Amit en egy szotarba gondoltam.Ami igy nezne ki:
loves={hanyadik{
"lovesek":egy sor
"hanyat lottek":len(sor)
}
}
"""
loves = {}
n=0
with open("verseny.txt", "rt",encoding="utf-8") as f:
    for s in f:
        sor = s.replace("\n", "")
        n+=1
        if n != 1:
            loves[n-1] = {}
            loves[n-1]["sor"] = sor
            loves[n-1]["hossza"] = len(sor)
            loves[n-1]["pont"] = int(loertek(sor))
#print(loves)
"""with open('sem.txt', 'wt',encoding="utf-8") as h:
    for g,v in loves.items():
        h.write("{0}:{1}\n".format(g, v))
"""
print("2. feladat")
"""ki kell irni azok a versenyzok rajtszamat akik egymas utan 2 szer betalaltak."""
print("Az egymast kovetoen tobbszor talalo versenyzok: {}".format(" ".join([str(k) for k,v in loves.items() if "++" in v["sor"]])))

print("3. feladat")
"""Ki kell ini hogy melyik versenyzo adta le a legtobb lovest."""
alma = []
for v in sorted(loves.values(), key=lambda v:v["hossza"]):
    alma.append(v["hossza"])
for k,a in loves.items():
    if a["hossza"] == alma[-1]:
        print("A legtobb lovest leado versenyzo rajtszama: {}".format(k))
#print("4. feladat")
"""Fuggveny keszites. Felul van mivel az alap szotar elkeszitesere is hasznalnom kellet."""

print("5. feladat")
"""Be kell kerni a felhasznalotol egy loves szamot."""
bekeres = int(input("Adjon meg egy rajtszamot! "))

"""Hanyadik lovesei talaltak a bekert rajtszamunak?"""
talalat = []
for k,v in loves.items():
    if k == bekeres:
        for h, g in enumerate(v["sor"]):
            if g == "+":
                talalat.append(str(h+1))
print("5a. feladat: Celt ero lovesek: {}".format(" ".join(talalat)))

"""hany korongot talalt el osszesen?"""
print("5b. feladat: Az eltalalt korongok szama: {}".format(len(talalat)))

"""milyen hosszu volt a leghosszabb kibatlan lovessorozata."""
hossz = 0
for k, a in loves.items():
    if k == bekeres:
        if "+++++++" in a["sor"]:
            hossz = 7
        elif "++++++" in a["sor"]:
            hossz = 6
        elif "+++++" in a["sor"]:
            hossz = 5
        elif "++++" in a["sor"]:
            hossz = 4
        elif "+++" in a["sor"]:
            hossz = 3
        elif "++" in a["sor"]:
            hossz = 2
        elif "+" in a["sor"]:
            hossz = 1
print("5c. feladat: A leghosszabb hibatlan sorozat hossza: {}".format(hossz))

"""hany pontot ert el?"""
for k, a in loves.items():
    if k == bekeres:
        print("5d. feladat: A versenyzo pontszama: {}".format(loertek(a["sor"])))   

#print("6. feladat")
"""Elo kell allitani a sorrend.txt--t."""
n = 0
pont = []
szotar = {}
elozo = int()
for v in sorted(loves.values(), key=lambda v:v["pont"], reverse=True):
        pont.append(v["pont"])
#print(pont)
for k,v in loves.items():
    for h in range(0,len(pont)):
            if pont[h] == v["pont"]:
                if pont[h] != elozo:
                    szotar[h+1] = {}
                    szotar[h+1]["hany"] = k
                    szotar[h+1]["pont"] = pont[h]
                else:
                    szotar[h] = {}
                    szotar[h]["hany"] = k
                    szotar[h]["pont"] = pont[h]

            elozo = pont[h]
#print(szotar)
with open("sorrend.txt", "wt", encoding="utf-8") as g:
    for j,f in szotar.items():
        g.write("{0}\t{1}\t{2}\n".format(j,f["hany"],f["pont"]))