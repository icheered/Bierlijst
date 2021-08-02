import random


def get_random_color_hex():
    return "#" + str(hex(random.randint(0, 16777215)))[2:]
