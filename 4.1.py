f = open('instrukcje.txt', 'r')
dlg = 0
for linia in f:
    x = linia.split()
    if x[0] == 'DOPISZ':
        dlg = dlg + 1
    if x[0] == 'USUN':
        dlg = dlg - 1
print(dlg)