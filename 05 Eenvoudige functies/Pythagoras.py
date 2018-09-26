a = float(input())
b = float(input())

from math import sqrt

c = sqrt(pow(a,2) + pow(b,2))

print('In een rechthoekige driekhoek met rechthoekzijden a =', '{:.2f}'.format(a), 'en b =', '{:.2f}'.format(b), 'is de schuine zijde', '{:.2f}'.format(c))
