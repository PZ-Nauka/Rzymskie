mapa = {
    1: "I",
    4: "IV",
    5: "V",
    9: "IX",
    10: "X",
    40: "XL",
    50: "L",
    90: "XC",
    100: "C",
    400: "CD",
    500: "D",
    900: "CM",
    1000: "M"
}


liczba = 322

cyfry = []
cyfry.append(int(liczba/1000))
cyfry.append(int((liczba%1000)/100))
cyfry.append(int(liczba%100/10))
cyfry.append(int(liczba%10))

print(liczba)
print(cyfry[0])
print(cyfry[1])
print(cyfry[2])
print(cyfry[3])

rzymska = ""
for i in range(0,len(cyfry)):
    if cyfry[i] == 0:
        continue

    # indeks 0 czyli tysiace
    if i == 0:
        rzymska += mapa[1000]

    # indeks 1 czyli setki
    if i == 1:
        if 1 <= cyfry[i] <= 3:
            rzymska += cyfry[i] * mapa[100]
        if cyfry[i] == 4:
            rzymska += mapa[400]
        if cyfry[i] == 5:
            rzymska += mapa[500]
        if 6 <= cyfry[i] <= 8:
            rzymska += mapa[500] + (cyfry[i]-5)*mapa[100]
        if cyfry[i] == 9:
            rzymska += mapa[900]

    # indeks 2 czyli dziesiatki
    if i == 2:
        if 1 <= cyfry[i] <= 3:
            rzymska += cyfry[i] * mapa[10]
        if cyfry[i] == 4:
            rzymska += mapa[40]
        if cyfry[i] == 5:
            rzymska += mapa[50]
        if 6 <= cyfry[i] <= 8:
            rzymska += mapa[50] + (cyfry[i]-5)*mapa[10]
        if cyfry[i] == 9:
            rzymska += mapa[90]

    # indeks 3 czyli jednosci
    if i == 3:
        if 1 <= cyfry[i] <= 3:
            rzymska += cyfry[i] * mapa[1]
        if cyfry[i] == 4:
            rzymska += mapa[4]
        if cyfry[i] == 5:
            rzymska += mapa[5]
        if 6 <= cyfry[i] <= 8:
            rzymska += mapa[5] + (cyfry[i]-5)*mapa[1]
        if cyfry[i] == 9:
            rzymska += mapa[9]

print("rzymska: " + rzymska)


