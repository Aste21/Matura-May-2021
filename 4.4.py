f = open('instrukcje.txt', 'r')
w = []
alfabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for linia in f:
    x = linia.split()
    if x[0] == 'DOPISZ':
        w.append(x[1])
    if x[0] == 'USUN':
        w.pop()
    if x[0] == 'ZMIEN':
        w[len(w)-1] = x[1]
    if x[0] == 'PRZESUN':
        if x[1] in w:
            i = w.index(x[1])
            litera = w[i]
            i_2 = alfabet.index(litera)+1
            i_2 = i_2%26
            litera = alfabet[i_2]
            w[i] = litera



print(''.join(w))
print(w)