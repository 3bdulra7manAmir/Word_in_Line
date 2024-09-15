#  finds and stores/ a specific word or sentence from a file called Target.txt and stores in result.txt
from datetime import datetime
import time
import subprocess as sp
import keyboard

#  targetedWord = input("Go ahead Alpha!: ")
#  print("Your String is : " + targetedWord)

programName = "C:\\Program Files (x86)\\Microsoft VS Code\\Code.exe"
sp.Popen([programName, "Incoming.txt"])

print("Press Enter when You are done Pasting The Lines!")
x = True
while x:
    if keyboard.is_pressed("Enter"):
        x = False

with open("Incoming.txt") as file1:
    #file1.write(targetedWord)
    for line in file1:
        if line.startswith("[ WARNING ]"):
            f = open("Outcoming.txt", "a")
            f.write(line)
            f.close()
            print(line)

sp.Popen([programName, "Outcoming.txt"])
current_dateTime = datetime.now()
print("Finished!...")
time.sleep(3)
