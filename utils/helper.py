import random


def choose_random(items, count):
    count = min(count, len(items))
    return random.sample(items, count)