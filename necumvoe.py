
#Algoritmus na nalezení největšího čísla ze seznamu čísel

while True:
    try:
        zadej = input("""
        
Zadej čísla oddělená mezerou: """)
        print()
        zadej = zadej.strip()
        zadej = zadej.split(" ")
        hodnoty = []
        for i in zadej:
            try:
                hodnoty.append(float(i))
            except:
                pass
        vysledek = hodnoty[0]
        kolo = 0
        print("Zadaná čísla byla: ", end="")
        for i in hodnoty:
            kolo += 1
            if len(hodnoty) != kolo:
                print(str(i)+",", end=" ")
            else:
                print(str(i))
            if i > vysledek:
                vysledek = i
            else:
                pass
        print("Největší z čísel bylo číslo:", vysledek)
    except:
        print("Musíš zadat alespoň jedno číslo!")