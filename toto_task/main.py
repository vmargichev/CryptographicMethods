import random

def toto_deal():
    toto_list = []
    for i in range(0,6):
        toto_list.append(random.randint(1,49))
    return toto_list

toto_game = toto_deal()
print(toto_game)
