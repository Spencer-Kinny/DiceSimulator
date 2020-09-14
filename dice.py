import random

def diceFace(x):
    switcher = {
        1: "------------\n|          |\n|    0     |\n|          |\n------------\n",
        2: "------------\n|          |\n|   0 0    |\n|          |\n------------\n",
        3: "------------\n|    0     |\n|    0     |\n|    0     |\n------------\n",
        4: "------------\n|   0 0    |\n|          |\n|   0 0    |\n------------\n",
        5: "------------\n|   0 0    |\n|    0     |\n|   0 0    |\n------------\n",
        6: "------------\n|   0 0    |\n|   0 0    |\n|   0 0    |\n------------\n",
    }
    return switcher.get(x, "nothing")
while(True):
    c = input("Press y to shake dice:")
    if(c != 'y'):
        break;
    x = random.randint(1,6)
    print(diceFace(x))
print("Thanks for playing!!!")
