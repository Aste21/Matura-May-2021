f = open('instrukcje.txt', 'r')
z = 0
max = 1
c = 1
for linia in f:
    x = linia.split()
    if z == 0 :
        ost = x[0]
    else:
        if ost == x[0]:
            c += 1
        else:
            if c > max:
                max = c
                rodzaj = ost
            c = 1
            ost = x[0]
    z += 1
print(f'rodzaj instrukcji - {rodzaj}, długość ciągu - {max}')

