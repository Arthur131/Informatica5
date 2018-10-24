totaal = 0
prijs = float(input('prijs product:'))

while prijs > 0:
    totaal+= prijs
    prijs = float(input('prijs product:'))
print('De totale prijs is € {:.2f}'.format(totaal))


