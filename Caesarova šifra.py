import string
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

posun = 69420

seznam = ' !"#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz{|}~\\€' + "'" + "ě" + "š" + "č" + "ř" + "ž" + "ý" + "á" + "í" + "é" + "ú" + "ů" + "ň" + "Ě" + "Š" + "Č" + "Ř" + "Ž" + "Ý" + "Á" + "Í" + "É" + "Ú" + "Ů" + "Ň"
alpha = []
for i in seznam:
    alpha.append(i)
print("Pro šifrování napiš před větu 1 a pro dešifrování napiš 2 (1Ahoj)\n")
screen = ["Pro šifrování napiš před větu 1 a pro dešifrování napiš 2 (1Ahoj)\n"]

while True:
    inp = input("")
    cls()
    for i in range(len(screen)):
        print(screen[i])
    print(inp[1:], end="   ")
    if inp[0] == "1":

        inputlist = []
        koloinputlist = 1
        for i in range(len(inp)-1):
            inputlist.append(inp[koloinputlist])
            koloinputlist += 1

        outputlist = []

        for i in inputlist:
            outputlist.append((alpha.index(i)+posun)%len(alpha))

        finalstring = ""

        for i in outputlist:
            finalstring = finalstring + alpha[i]

        print("----->   " + finalstring)

    elif inp[0] == "2":

        inputlist = []
        koloinputlist = 1
        for i in range(len(inp)-1):
            inputlist.append(inp[koloinputlist])
            koloinputlist += 1

        outputlist = []

        for i in inputlist:
            outputlist.append((alpha.index(i)-posun)%len(alpha))

        finalstring = ""

        for i in outputlist:
            finalstring = finalstring + alpha[i]

        print("----->   " + finalstring)
    else:
        pass
    pridat = inp[1:] + "   ----->   " + finalstring
    screen.append(pridat)
    rozcesti = None

