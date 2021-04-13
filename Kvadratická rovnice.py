import time
import os
import math

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
while True:
    cls()
    print("Kalkulátor kvadratické rovnice: ax**2 + bx + c = 0")
    try:
        a = float(input("Zadej a: "))
        b = float(input("Zadej b: "))
        c = float(input("Zadej c: "))

        if a == 0:
            print("a = 0 takže to je lineární rovnice")
            x = (-c) / b
            print("x = ", x)
            os.system("pause")
        else:
            D = b**2 - 4 * a * c

            if D < 0:
                print("Nemá řešení, diskriminant je: ", D)
                os.system("pause")
            elif D == 0:
                x = -b / 2 * a
                print("X se rovná: " + x, "a diskriminant je: ", D)
                os.system("pause")
            else:
                x1 = (-b + math.sqrt(D)) / (2 * a)
                x2 = (-b - math.sqrt(D)) / (2 * a)
                print("Rovnice má dvě řešení: ", x1, x2, "a diskriminant je: ", D)
                os.system("pause")
    except:
        cls()
        print("Zadej číslo, ne písmena!")
        time.sleep(2)

