import time
import random
num = int(time.time())
print("Hi, what characters do you currently have in your roster of Genshin?\n")

geo = ["Albedo", "Itto", "Gorou", "Ningguang", "Noelle", "Geo-Traveler", "Yun Jin", "Zhongli"]
cryo = ["Aloy", "Chongyun", "Diona", "Eula", "Ganyu", "Kaeya", "Ayaka", "Layla", "Qiqi", "Rosaria", "Shenhe", "Mika"]
pyro = ["Amber", "Bennett", "Diluc", "Hu Tao", "Klee", "Thoma", "Xiangling", "Xinyan", "Yanfei", "Yoimiya", "Dehya"]
hydro = ["Barbara", "Candace", "Ayato", "Mona", "Nilou", "Kokomi", "Tartaglia", "Xingqui", "Yelan"]
electro = ["Beidou", "Cyno", "Dori", "Fischl", "Keqing", "Sara", "Kuki", "Lisa", "Raiden", "Razor", "Electro-Traveler", "Yae"]
dendro = ["Collei", "Tighnari", "Nahida", "Dendro-Traveler", "Alhaitham", "Yaoyao"]
anemo = ["Faruzan", "Jean", "Kazuha", "Sayu", "Heizou", "Sucrose", "Anemo-Traveler", "Venti", "Wanderer", "Xiao"]
elements = [geo, cryo, pyro, hydro, electro, dendro, anemo]
chars = []
print("To input a character into the randomizer, select an element and then choose the characters listed: \n")
ele = 10
while (ele not in range(0, 8) and ele != 0 and ele != "x"):
        ele = input("What element would you like to choose from? "
                    "\ngeo=1, cryo=2, pyro=3, hydro=4, electro=5, dendro=6 or anemo=7"
                    "\n(if you are done with selection, just type '0')"
                    "\n(if you want to exit the randomizer, type 'x')\n")
        if ele.isdigit():
            ele = int(ele)

while (ele != 0 and ele != "x"):
    c = geo
    if (ele == 1):
        c = geo
    elif (ele == 2):
        c = cryo
    elif (ele == 3):
        c = pyro
    elif (ele == 4):
        c = hydro
    elif (ele == 5):
        c = electro
    elif (ele == 6):
        c = dendro
    elif (ele == 7):
        c = anemo
    print("Choosable characters are:")
    for i in c:
        print(i)
    ch = input("Which characters do you want to choose?\n(0 to exit)\n")
    while (ch != "0"):
        if ch in c and ch not in chars:
            chars.append(ch)
            c.remove(ch)
        else:
            print("No character given was found or character has already been selected")
        for i in c:
            print(i)
        print("------------")
        ch = input("Which characters do you want to choose?\n(0 to exit)\n")
    ele = input("What element would you like to choose from \n"
                "geo=1, cryo=2, pyro=3, hydro=4, electro=5, dendro=6 or anemo=7\n"
                "(if you are done with selection, just type 0)\n"
                "\n(if you want to exit the randomizer, type 'x')\n")
    if ele.isdigit():
        ele = int(ele)
    while (ele not in range(0, 8) and ele != 0 and ele != "x"):
        ele = input("What element would you like to choose from? "
                    "\ngeo=1, cryo=2, pyro=3, hydro=4, electro=5, dendro=6 or anemo=7"
                    "\n(if you are done with selection, just type '0')"
                    "\n(if you want to exit the randomizer, type 'x')\n")
        if ele.isdigit():
            ele = int(ele)
    if len(chars) < 9 and ele != "x":
        print("Currently the minimum 9 characters haven't been given!")
        print("Please input more characters to the randomizer")
while ele == 0 and len(chars) > 8:
    print("Time to start the randomizer!")
    print("")
    char = chars
    cho = []
    for i in range(4):
        cha = random.choice(char)
        cho.append(cha)
        char.remove(cha)
    print("The characters for the first half are:")
    print("----------------")
    for c in cho: print(c)
    print("----------------")
    cho = []

    for i in range(4):
        cha = random.choice(char)
        cho.append(cha)
        char.remove(cha)
    print("The characters for the second half are:")
    print("----------------")
    for c in cho: print(c)
    print("----------------")
    ele = input("If you are happy with the results then just press enter\n"
                "If you want to redo the randomizer, type 0\n")
    if ele.isdigit():
        ele = int(ele)
