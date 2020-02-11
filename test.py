a = 'm/t/psc'
b = '3/5/7'
c = '7'
b_spil = b.split('/')
print(b_spil)
for i in b_spil:
    if i == c:
        n = len(i)
        print(n)
    else:
        print(9)