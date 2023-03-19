#  reads directory files names and store it without extension then write the result into a file called temp.txt
import os
from datetime import datetime
import time

targetedPath = input("Go ahead Alpha!: ")
print("Your Path is : " + targetedPath)
fileName = input("precache file name: ")
print("Your precache file name is : " + fileName)

for x in os.listdir(targetedPath):
    if x.endswith(".xmodel_export"):
        f = open(""f"{fileName}.txt", "a")
        f.write("precacheitem("f"\"{x}\""");" + "\n")
        f.close()
        print(x)
    elif x.endswith(".json"):
        f = open(""f"{fileName}.txt", "a")
        f.write("precacheitem("f"\"{x}\""");" + "\n")
        f.close()
        print(x)

current_dateTime = datetime.now()
print("Finished!...")
time.sleep(3)