#Da se napravi programa koja bi bila za potrebite vo nekoj prodavnica. Korisnikot da moze vo edna lista do go dodava imeto na produktot, vo druga cenata. Koga ke gi dodade site produkti da se ispecati "fiskalna smetka" vo format (Produkt: Cena) i da se ispecati kolku vkupno treba da plati korisnikot.
#*HINT: imate razlicni nacini na koi mozete da ja resite zadacata. PROBAJTE da napravite da moze da korisnikot moze vnesuva kolku produkti saka tolku(da ne kazuva na pocetok kolku produkti ke vnese)

#*OPCIONALNO: Dodadete funkcionalnost da moze korisnikot da "plati" i da se presmeta kolku treba da mu se vrati kusur.

produkti={}
ceni=[]
ch='d'
while ch=='d' or ch=='D':
    name=input("Vnesi ime na produkt : ")
    price=eval(input("Vnesi cena za produkt : "))
    ceni.append(price)
    produkti[name]=price
    ch=input("Dali sakate da vnesete nov produkt (D/N) : ")
print(produkti)
print(ceni)
zbir = sum(ceni)
print ("Vkupno za plakanje", zbir ,"denari")

cash = eval(input("Primena suma: "))
if cash < zbir:
    print("Nemate dovolno sredstva za kupuvanje na site produkti")
else:
    print("za vrakanje", cash-zbir, "denari")
