targetedWord = 'xanim'
with open("Target.txt") as file1:
    for line in file1:
        if line.startswith(targetedWord):
            f = open("result.txt", "a")
            f.write(line)
            f.close()
            print(line)
