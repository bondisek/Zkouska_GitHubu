from PyQt5 import QtWidgets
from PyQt5 import QtGui

app = QtWidgets.QApplication([])

# Hlavní okno
main_okno = QtWidgets.QWidget()
main_okno.setWindowTitle('Nase skvělá grafická aplikace')

# Layout pro hlavní okno
layout_vedle_sebe = QtWidgets.QHBoxLayout()
main_okno.setLayout(layout_vedle_sebe)

# Nápis
label_napis = QtWidgets.QLabel('Ahoj, klikni na tlačítko')
# Přidáním do layoutu se nápis automaticky stane potomkem hlavního okna
layout_vedle_sebe.addWidget(label_napis)

# Tlačítko
button_tlaciko = QtWidgets.QPushButton('Zmáčkni mě')
layout_vedle_sebe.addWidget(button_tlaciko)

# Vstupní políčko
vstupni_pole = QtWidgets.QLineEdit()
layout_vedle_sebe.addWidget(vstupni_pole)

# Vnořený Layout
layout_nadsebou = QtWidgets.QVBoxLayout()
layout_vedle_sebe.addLayout(layout_nadsebou)

# Tlačítko
button_tlaciko_1 = QtWidgets.QPushButton('A')
button_tlaciko_2 = QtWidgets.QPushButton('B')
button_tlaciko_3 = QtWidgets.QPushButton('C')
layout_nadsebou.addWidget(button_tlaciko_1)
layout_nadsebou.addWidget(button_tlaciko_2)
layout_vedle_sebe.addWidget(button_tlaciko_3)

# onlyInt = QtGui.QIntValidator() # hlídač čísel
# vstupni_pole.setValidator(onlyInt)

# Funkcionalita
def zmen_napis():
    try:
        vstupni_text = vstupni_pole.text()
    #    vstupni_cislo = int(vstupni_text)
        vstupni_hodnoty = vstupni_text.split(" ")  # rozdělí nápis na více nápisů (do Listu nápisů) "487 45 2" -> ["487", "45", "2"]
        vstupni_cisla = []  # připravíme prázdný List
        for prvek in vstupni_hodnoty: # projdeme všechny nápisy (znaky) z vstupnich_znaky
            vstupni_cisla.append(int(prvek)) # každý převedeme na integer a uložíme do připraveného Listu
        label_napis.setText(str(vstupni_cisla))
    except ValueError as exc: # co se má stát, když nastane ValueError
        label_napis.setText("Zadal jsi hodnotu, která nejde převést na celé číslo")
        print("Nastala chyba:\n", type(exc))
    except Exception as exc:
        label_napis.setText("Nastala jiná chyba")
        print("Nastala chyba:\n", type(exc))

button_tlaciko.clicked.connect(zmen_napis)

# Spuštění
main_okno.show()

app.exec()
