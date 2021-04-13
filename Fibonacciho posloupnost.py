while True:
    print()
    první_hodnota = int(input("Zadej první hodnotu: "))
    kolik_cyklů = int(input("Zadej kolik má být výstupních hodnot: "))

    první = první_hodnota
    druhá = první_hodnota
    print("(1)"+str(první), "(2)"+str(druhá), end=" ")

    for i in range(kolik_cyklů-2):
        třetí = první + druhá
        druhá = první
        první = třetí
        print("("+str(i+3)+")"+str(třetí), end=" ")