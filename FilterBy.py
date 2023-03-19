#  finds and stores/ a specific word or sentence from a file called Target.txt and stores in result.txt
from datetime import datetime
import time

targetedWord = input("Go ahead Alpha!: ")
print("Your String is : " + targetedWord)

with open("Incoming.txt") as file1:
    for line in file1:
        if line.startswith(targetedWord):
            f = open("Outcoming.txt", "w")
            f.write(line)
            f.close()
            print(line)

current_dateTime = datetime.now()
print("Finished!...")
time.sleep(3)
