# Matura-May-2021
Matura May 2021
Task:

    Zadanie 4. Neon cyfrowy
Pewna firma przygotowuje wyświetlanie napisów złożonych z wielkich liter alfabetu
angielskiego. Na początku napis jest pusty (nie zawiera liter). W pliku instrukcje.txt
podanych jest 2000 instrukcji, które wykonuje automat do generowania napisu. Każda
z instrukcji składa się z polecenia, spacji oraz pojedynczego znaku. Polecenia są czterech
rodzajów:
DOPISZ litera – oznacza, że na końcu napisu trzeba dopisać pojedynczą literę;
ZMIEN litera – oznacza, że ostatnią literę aktualnego napisu należy zmienić na podaną
literę (możesz założyć, że napis jest niepusty);
USUN 1 – oznacza, że należy usunąć ostatnią literę aktualnego napisu (możesz
założyć, że napis jest niepusty);
PRZESUN litera – oznacza, że pierwsze od lewej wystąpienie podanej litery w napisie należy
zamienić na następną literę w alfabecie (jeśli litera to A, to należy zamienić
na B, jeśli B, to na C itd.) Literę Z należy zamienić na A. Jeśli litera nie
występuje w napisie, nie należy nic robić.
Przykład:
Dany jest następujący ciąg instrukcji:
DOPISZ A
DOPISZ B
DOPISZ C
USUN 1
DOPISZ D
ZMIEN B
DOPISZ E
PRZESUN B
Po wykonaniu pierwszych trzech instrukcji napis będzie miał postać ABC, potem AB, ABD,
ABB, ABBE, wreszcie ostatnia instrukcja zamieni pierwsze B na C, więc ostatecznie powstały
napis to ACBE.
Napisz program (lub kilka programów), który(-e) znajdzie(-dą) odpowiedzi na poniższe
pytania. Każdą odpowiedź zapisz w pliku wyniki4.txt i poprzedź ją numerem
oznaczającym zadanie.
Do dyspozycji masz również plik przyklad.txt, w którym znajduje się tylko 20 instrukcji –
odpowiedzi dla tego pliku podane są w treściach zadań, możesz więc sprawdzać na nim
działanie swojego programu. Pamiętaj, że Twój program musi ostatecznie działać dla 2000
instrukcji.


    Zadanie 4.1. (0–2)
Oblicz całkowitą długość napisu po wykonaniu wszystkich instrukcji z pliku
instrukcje.txt.
Dla pliku przyklad.txt długością napisu jest liczba 10. 


    Zadanie 4.2. (0–2)
Znajdź najdłuższy ciąg występujących kolejno po sobie instrukcji tego samego rodzaju. Jako
odpowiedź podaj rodzaj instrukcji oraz długość tego ciągu. Istnieje tylko jeden taki ciąg.
Dla pliku przyklad.txt odpowiedzią jest: rodzaj instrukcji – DOPISZ, długość ciągu – 5.


    Zadanie 4.3. (0–3)
Oblicz, która litera jest najczęściej dopisywana (najczęściej występuje w instrukcji DOPISZ).
Podaj tę literę oraz ile razy jest dopisywana. Istnieje tylko jedna taka litera.
Dla pliku przyklad.txt odpowiedzią jest litera U, dopisywana 3 razy.


    Zadanie 4.4 (0–4)
Podaj napis, który powstanie po wykonaniu wszystkich instrukcji z pliku instrukcje.txt.
Dla pliku przyklad.txt wynikiem jest napis ALANTURING. 
