r = float(input('geef de afstand: '))
Q1 = 2.0 * (10 ** (-6))
Q2 = 1.0 * (10 ** (-6))
k = 8.99 * (10 ** 13)

coulombkracht = k * ((Q1*Q2) / (r ** 2))

print(coulombkracht)