while True:
    začátek = int(input("Počáteční číslo: "))

    výsledek = 1

    for i in range(začátek):
        výsledek = výsledek*(i+1)

    print(výsledek)