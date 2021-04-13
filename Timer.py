import time
from PyQt5 import QtWidgets
from PyQt5.QtCore import *

app = QtWidgets.QApplication([])

main = QtWidgets.QWidget()

main.setWindowTitle("Timer")
layout = QtWidgets.QHBoxLayout()
LSloupec = QtWidgets.QVBoxLayout()
RSloupec = QtWidgets.QVBoxLayout()
layout.addLayout(LSloupec)
layout.addLayout(RSloupec)
HLayout = QtWidgets.QHBoxLayout()
VLayoutS = QtWidgets.QVBoxLayout()
VLayoutM = QtWidgets.QVBoxLayout()
VLayoutH = QtWidgets.QVBoxLayout()
VLayoutD = QtWidgets.QVBoxLayout()
VLayoutW = QtWidgets.QVBoxLayout()
VLayoutY = QtWidgets.QVBoxLayout()
HLayoutMain = QtWidgets.QHBoxLayout()
VLayoutBtn = QtWidgets.QVBoxLayout()

casomira = QtWidgets.QLabel()
casomira.setStyleSheet("border:3px solid black; font-size:50px; padding:20px")
casomira.setText("00:00:00:00:00:00")
casomira.setAlignment(Qt.AlignCenter)
casomira.setMaximumHeight(100)


pocet_kol = QtWidgets.QLabel()
pocet_kol.setStyleSheet("border:3px solid black; font-size: 50px; padding:20px")
pocet_kol.setText("0")
pocet_kol.setAlignment(Qt.AlignCenter)
pocet_kol.setMaximumHeight(100)


zadani_casu_s = QtWidgets.QSpinBox()
zadani_casu_s.setFixedSize(50, 25)
zadani_casu_s.setStyleSheet("border:3px solid black; font-size: 15px")
zadani_casu_s.setAlignment(Qt.AlignCenter)
zadani_casu_s.setRange(0, 59)

zadani_casu_m = QtWidgets.QSpinBox()
zadani_casu_m.setFixedSize(50, 25)
zadani_casu_m.setStyleSheet("border:3px solid black; font-size: 15px")
zadani_casu_m.setAlignment(Qt.AlignCenter)
zadani_casu_m.setRange(0, 59)

zadani_casu_h = QtWidgets.QSpinBox()
zadani_casu_h.setFixedSize(50, 25)
zadani_casu_h.setStyleSheet("border:3px solid black; font-size: 15px")
zadani_casu_h.setAlignment(Qt.AlignCenter)
zadani_casu_h.setRange(0, 23)

zadani_casu_d = QtWidgets.QSpinBox()
zadani_casu_d.setFixedSize(50, 25)
zadani_casu_d.setStyleSheet("border:3px solid black; font-size: 15px")
zadani_casu_d.setAlignment(Qt.AlignCenter)
zadani_casu_d.setRange(0, 6)

zadani_casu_w = QtWidgets.QSpinBox()
zadani_casu_w.setFixedSize(50, 25)
zadani_casu_w.setStyleSheet("border:3px solid black; font-size: 15px")
zadani_casu_w.setAlignment(Qt.AlignCenter)
zadani_casu_w.setRange(0, 51)

zadani_casu_y = QtWidgets.QSpinBox()
zadani_casu_y.setFixedSize(50, 25)
zadani_casu_y.setStyleSheet("border:3px solid black; font-size: 15px")
zadani_casu_y.setAlignment(Qt.AlignCenter)
zadani_casu_y.setRange(0, 99)


zadani_opakovani = QtWidgets.QSpinBox()
zadani_opakovani.setFixedSize(100, 25)
zadani_opakovani.setStyleSheet("border:3px solid black; font-size: 15px")
zadani_opakovani.setAlignment(Qt.AlignCenter)
zadani_opakovani.setRange(0, 1000000)


start = QtWidgets.QPushButton()
start.setText("Start")


stop = QtWidgets.QPushButton()
stop.setText("Stop")

popisekS = QtWidgets.QLabel("Sek")
popisekM = QtWidgets.QLabel("Min")
popisekH = QtWidgets.QLabel("Hod")
popisekD = QtWidgets.QLabel("Den")
popisekW = QtWidgets.QLabel("Týd")
popisekY = QtWidgets.QLabel("Rok")


VLayoutY.addWidget(zadani_casu_y)
VLayoutY.addWidget(popisekY)
VLayoutW.addWidget(zadani_casu_w)
VLayoutW.addWidget(popisekW)
VLayoutD.addWidget(zadani_casu_d)
VLayoutD.addWidget(popisekD)
VLayoutH.addWidget(zadani_casu_h)
VLayoutH.addWidget(popisekH)
VLayoutM.addWidget(zadani_casu_m)
VLayoutM.addWidget(popisekM)
VLayoutS.addWidget(zadani_casu_s)
VLayoutS.addWidget(popisekS)

HLayoutMain.addWidget(casomira)
HLayoutMain.addWidget(pocet_kol)
LSloupec.addLayout(HLayoutMain)
LSloupec.addLayout(HLayout)
HLayout.addLayout(VLayoutY)
HLayout.addLayout(VLayoutW)
HLayout.addLayout(VLayoutD)
HLayout.addLayout(VLayoutH)
HLayout.addLayout(VLayoutM)
HLayout.addLayout(VLayoutS)
HLayout.addLayout(VLayoutBtn)
VLayoutBtn.addWidget(start)
VLayoutBtn.addWidget(stop)
LSloupec.addWidget(zadani_opakovani)


def odpocet():
    jedna = 1
    s = zadani_casu_s.text()
    m = zadani_casu_m.text()
    h = zadani_casu_h.text()
    d = zadani_casu_d.text()
    w = zadani_casu_w.text()
    y = zadani_casu_y.text()
    global cas
    cas = [s, m, h, d, w, y]
    casy = []

    celkcas = 0
    celkcas += int(cas[0])
    celkcas += int(cas[1]) * 60
    celkcas += int(cas[2]) * 3600
    celkcas += int(cas[3]) * 86400
    celkcas += int(cas[4]) * 604800
    celkcas += int(cas[5]) * 31536000
    print(celkcas)
    global temp
    temp = celkcas




    if int(zadani_opakovani.text()) == 0:
        while jedna == 1 and celkcas != -1:
            cas[5] = celkcas // 31536000
            celkcas = celkcas % 31536000
            cas[4] = celkcas // 604800
            celkcas = celkcas % 604800
            cas[3] = celkcas // 86400
            celkcas = celkcas % 86400
            cas[2] = celkcas // 3600
            celkcas = celkcas % 3600
            cas[1] = celkcas // 60
            celkcas = celkcas % 60
            cas[0] = celkcas

            for i in cas:
                if len(str(i)) == 1:
                    cas = "0" + str(i)
                    casy.append(cas)
                else:
                    casy.append(str(i))

            text = casy[5]+":"+casy[4]+":"+casy[3]+":"+casy[2]+":"+casy[1]+":"+casy[0]
            print(text)
            time.sleep(1)

            casomira.setText(text)

            temp -= 1
            celkcas = int(temp)
            cas = ["0", "0", "0", "0", "0", "0"]
            casy.clear()


"""
    for i in range(int(zadani_opakovani.text())):
        while jedna == 1 and "00" not in casy[0] and "00" not in casy[1] and "00" not in casy[2] and "00" not in casy[3] and "00" not in casy[4] and "00" not in casy[5]:
            text = casy[5]+":"+casy[4]+":"+casy[3]+":"+casy[2]+":"+casy[1]+":"+casy[0]
            print(text)
            casomira.setText(text)
            time.sleep(1)
            casy[0] = str(int(casy[0])-1)
            stop.clicked.connect(odecist)
"""
def odecist():
    global jedna
    jedna = 0

jedna = 1

start.clicked.connect(odpocet)
stop.clicked.connect(odecist)

main.setLayout(layout)

main.show()
app.exec()
