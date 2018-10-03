#Indien vader werd opgegeven, print je: Krokodil geeft kind terug.
#Indien krokodil werd opgegeven, print je: Krokodil eet kind op.
#In alle andere geval toon je: Moe van het denken.

naam = input('geef naam:')

if naam == 'vader':
    print('Krokodil geeft kind terug')
elif naam == 'krokodil':
    print('Krokodil eet kind op')
else:
    print('Moe van het denken')