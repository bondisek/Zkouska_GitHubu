import keyboard
import time

lul = int(input("Nečum: "))

print("5 sekund")
time.sleep(5)

keyboard.write(str(abs(lul)))
keyboard.press("Return")
while True:
    keyboard.write(str(abs(lul)+1)+"  "+str(abs(lul)+2)+"  "+str(abs(lul)+3)+"  "+str(abs(lul)+4)+"  "+str(abs(lul)+5)+"  "+str(abs(lul)+6)+"  "+str(abs(lul)+7)+"  "+str(abs(lul)+8)+"  "+str(abs(lul)+9)+"  "+str(abs(lul)+10)+"  ")
    keyboard.press("Return")
    lul += 10
    time.sleep(1)
"""
text = str()
while True:
    text = str(text) + " " + str(lul)
    keyboard.write(str(text))
    keyboard.press("Return")
    lul += 1
    time.sleep(1)
"""



