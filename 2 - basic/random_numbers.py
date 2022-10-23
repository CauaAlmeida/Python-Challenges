import random

random_num = 0


def generateRandomNum():
    random_x = random.randint(0, 100)
    if random_x > 99:
        pass
    else:
        print(random_x)
        generateRandomNum()


generateRandomNum()
