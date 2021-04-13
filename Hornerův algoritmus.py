while True:
    ans = 0
    počet = 1
    hodnoty = []
    var = float(input("Napište proměnnou: "))
    while ans != "":
        ans = input("Napište "+str(počet)+". číslo nebo nechte prázdné: ")
        počet += 1
        try:
            hodnoty.append(float(ans))
        except:
            pass
    ans = hodnoty[-1]
    for i in range(1, len(hodnoty)):
        ans = (ans * var) + hodnoty[-1-i]
    print("Výsledek je: ", ans)