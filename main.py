while True:
    num = input("Napiš číslo: ")
    try:
        num = float(num)

        if num > 0:
            print("Číslo je kladné.")
        elif num < 0:
            print("Číslo je záporné.")
        else:
            print("Číslo je nula.")
    except:
        print("Napiš číslo, ne písmena!")