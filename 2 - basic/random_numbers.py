import random

random_num = 0

def generateRandomNum():
    random_num = random.randint(0,100)
    if random_num > 99:
        pass
    else:
        print(random_num)
        generateRandomNum()

generateRandomNum()