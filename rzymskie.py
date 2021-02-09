mapa_ara_rzy = {
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
mapa_rzy_ara = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000
}

    
    
    

def zamien_rz_do_ara(liczbaR):
    liczbaA = 0
    i = 0
    while i < len(liczbaR):
        
        if i == (len(liczbaR)-1):
            liczbaA += mapa_rzy_ara[liczbaR[i]]
        else:
            
            try:
                liczbaATemp = mapa_rzy_ara[liczbaR[i] + liczbaR[i+1]]
                i += 1
            except KeyError:
                liczbaATemp = mapa_rzy_ara[liczbaR[i]]
            
            liczbaA += liczbaATemp
            
        i += 1    
    
    return liczbaA


def najwiekszy_klucz(liczba):
    global mapa_ara_rzy
    
    for i in sorted(mapa_ara_rzy, reverse=True):
        if liczba >= i:
            return i
    
    return 0
    


def zamien_ara_do_rz(liczbaA):
    cyfry = [
        int(liczbaA/1000),
        int(liczbaA%1000-liczbaA%100),
        int(liczbaA%100-liczbaA%10),
        int(liczbaA%10)
    ]
    
    liczbaR = ""
    
    while liczbaA > 0:
        klucz = najwiekszy_klucz(liczbaA)
        liczbaR += mapa_ara_rzy[klucz]
        liczbaA -= klucz
        
    return liczbaR
    
    
boo = True    
while boo:
	try:
		liczbaR = [x for x in input().split(" ")]
	except:
		break
	
	Suma = zamien_rz_do_ara(liczbaR[0]) + zamien_rz_do_ara(liczbaR[1])
	print(zamien_ara_do_rz(Suma))


