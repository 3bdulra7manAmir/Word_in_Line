#  reads directory files names and store it without extension then write the result into a file called temp.txt

import os
z = "E:\\Ga me s\\Original Ga me s\\Battle.net\\Call of Duty - Modern Warfare 2 CR\\zonetool\\SC_weapon_con\\weapons"

for x in os.listdir(z):
    if x.endswith(".xmodel_export"):
        f = open("temp.txt", "w")
        f.write("precacheitem("f"\"{x}\""");" + "\n")
        f.close()
        print(x)
    # elif x.endswith(".xanim_export"):
    #     f = open("temp.txt", "w")
    #     f.write("precacheitem(   " + x + "   )" + "\n")
    #     f.close()
    #     print(x)
    elif x.endswith(".json"):
        f = open("temp.txt", "w")
        f.write("precacheitem("f"\"{x}\""");" + "\n")
        f.close()
        print(x)
