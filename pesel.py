import random

"""pesel = input("Wprowadź 11-cyfrowy numer PESEL: ")

print("Data urodzenia to " +
      str(pesel[4:6]) + "-" + str(pesel[2:4]) + "-19" + (str(pesel[0:2])))

if int(pesel[9]) % 2 == 0:
    print("Kobieta")
else:
    print("Męczyna")

p0 = str(int(pesel[0]) * 1)
p1 = str(int(pesel[1]) * 3)
p2 = str(int(pesel[2]) * 7)
p3 = str(int(pesel[3]) * 9)
p4 = str(int(pesel[4]) * 1)
p5 = str(int(pesel[5]) * 3)
p6 = str(int(pesel[6]) * 7)
p7 = str(int(pesel[7]) * 9)
p8 = str(int(pesel[8]) * 1)
p9 = str(int(pesel[9]) * 3)

suma = str(int(p0[-1]) + int(p1[-1]) + int(p2[-1]) + int(p3[-1]) + int(p4[-1]) +
           int(p5[-1]) + int(p6[-1]) + int(p7[-1]) + int(p8[-1]) + int(p9[-1]))

suma_kontrolna = 10 - int(suma[-1])

if suma_kontrolna == int(pesel[10]):
    print("PESEL poprawny, suma kontrolna się zgadza.")
else:
    print("Fałszywy PESEL")

"""

print("...:::Wygeneruj PESEL:::...")
data = input("Wprowadź datę urodzenia w formacie DDMMRRRR:  ")
plec = input("wybierz płeć M lub K:  ")

mez = [1, 3, 5, 7, 9]
kob = [0, 2, 4, 6, 8]
m = random.choice(mez)
k = random.choice(kob)
pole7 = random.randint(0, 9)
pole8 = random.randint(0, 9)
pole9 = random.randint(0, 9)

p0 = str(int(data[6]) * 1)
p1 = str(int(data[7]) * 3)
p2 = str(int(data[2]) * 7)
p3 = str(int(data[3]) * 9)
p4 = str(int(data[0]) * 1)
p5 = str(int(data[1]) * 3)
p6 = str(pole7 * 7)
p7 = str(pole8 * 9)
p8 = str(pole9 * 1)
p9m = str(m * 3)
p9k = str(k * 3)
sumamez = str(int(p0[-1]) + int(p1[-1]) + int(p2[-1]) + int(p3[-1]) + int(p4[-1]) +
              int(p5[-1]) + int(p6[-1]) + int(p7[-1]) + int(p8[-1]) + int(p9m[-1]))
sumakob = str(int(p0[-1]) + int(p1[-1]) + int(p2[-1]) + int(p3[-1]) + int(p4[-1]) +
              int(p5[-1]) + int(p6[-1]) + int(p7[-1]) + int(p8[-1]) + int(p9k[-1]))
suma_kontrolna_mez = 10 - int(sumamez[-1])
suma_kontrolna_kob = 10 - int(sumakob[-1])

facet = data[6] + data[7] + data[2] + data[3] + data[0] + data[1] + str(pole7) + str(pole8) + str(pole9) + str(m) + str(suma_kontrolna_mez)
baba = data[6] + data[7] + data[2] + data[3] + data[0] + data[1] + str(pole7) + str(pole8) + str(pole9) + str(k) + str(suma_kontrolna_kob)

#dorobic wariant zeby bylo w sumie 11 liczb, a nie np. 12 w razie czego
#dorobic wyjatki zeby nie wprowadzic blednych wartosci
#zrobic wersje okienkowa
#generowanie tozsamosci z imionami i nazwiskami

if plec == "M":
    print(facet)
if plec == "K":
    print(baba)

