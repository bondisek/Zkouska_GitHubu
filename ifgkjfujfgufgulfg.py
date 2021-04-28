cisla = [1, 2, 9, 3, 5, 8]
cisla.sort(reverse=True)
print(cisla)

def serazovac(*cisla):
    cisla = list(cisla)
    cisla.sort(reverse=True)
    print(cisla)

serazovac(1,8,9,5)





class Cisla:
    def __init__(self, cislo, definice):
        self.cislo = cislo
        self.definice = definice


    def vypis(self):
        print("Číslo je: " + str(self.cislo) + " a je " + self.definice)


dvojka = Cisla(2, "celé")


class CelaCisla(Cisla):
    def __init__(self, cislo, definice, delitelnost):
        super().__init__(cislo, definice)
        self.delitelnost = delitelnost



dvojka.vypis()

moc nečum


