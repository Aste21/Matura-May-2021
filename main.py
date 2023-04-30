def palindrom(slowo):
    for x in range(len(slowo)//2):
        if slowo[x] != slowo[len(slowo)-1-x]:
            return False
    return True

f = open('napisy.txt', 'r')
ile_cyfr = 0
wiersz_numer_haslo = 20
wiersz_numer = 0
pozycja_litery = 0
haslo = []
odpowiedz_3 = []
odpowiedz_4 = []
for linia in f:
    czy_bylo = False
    y = 0
    cyfry = 0
    numer = []
    wiersz_numer += 1
    slowo = linia.strip()
    for x in range (len(slowo)):
        if slowo[x].isdigit():
            ile_cyfr +=1
            cyfry += 1
    if wiersz_numer == wiersz_numer_haslo:
        haslo.append(slowo[pozycja_litery])
        wiersz_numer_haslo += 20
        pozycja_litery += 1
    palindrom_przod = slowo[len(slowo)-1] + slowo
    palindrom_tyl = slowo + slowo[0]
    if palindrom(palindrom_przod):
        odpowiedz_3.append(palindrom_przod[25])
    elif palindrom(palindrom_tyl):
        odpowiedz_3.append(palindrom_tyl[25])
    if cyfry%2 != 0:
        cyfry -= 1
    while cyfry>0:
        if slowo[y].isdigit():
            numer.append(slowo[y])
            cyfry -= 1
            czy_bylo = True
        if czy_bylo and cyfry % 2 == 0 and len(numer)>0  and int(''.join(numer)) >= 65 and int(''.join(numer)) <= 90:
            odpowiedz_4.append(int(''.join(numer)))
            numer = []
        y += 1
        if len(odpowiedz_4)>3:
            if odpowiedz_4[len(odpowiedz_4)-1] == 88 and odpowiedz_4[len(odpowiedz_4)-2] == 88 and odpowiedz_4[len(odpowiedz_4)-3] == 88:
                break
for z in range(len(odpowiedz_4)):
    odpowiedz_4[z] = chr(odpowiedz_4[z])
print(f"4.1:  {ile_cyfr}")
print(f"4.2:  {''.join(haslo)}")
print(f"4.3:  {''.join(odpowiedz_3)}")
print(f"4.4:  {''.join(odpowiedz_4)}")


