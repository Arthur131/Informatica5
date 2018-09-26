a = int(input())
b = int(input())
c = a + b

d = '{:>7} + {:<7} = {}'.format(a,b,c)
e = '{:>7} + {:<7} = {}'.format(a * 10,b * 10,c * 10)
f = '{:>7} + {:<7} = {}'.format(a * 100,b * 100,c * 100)
g = '{:>7} + {:<7} = {}'.format(a * 1000,b * 1000,c * 1000)
h = '{:>7} + {:<7} = {}'.format(a * 10000,b * 10000,c * 10000)

print(d)
print(e)
print(f)
print(g)
print(h)




