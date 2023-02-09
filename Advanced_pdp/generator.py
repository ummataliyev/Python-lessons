# Generators

import time

def answer():

    time.sleep(3)
    yield 21
    
    time.sleep(3)
    yield 42

    time.sleep(3)
    yield 63


# for a in answer():
#     print(a*a)

def counter(count: int):
    for i in range(count):
        time.sleep(1)
        yield i

# for c in counter(5):
#     # print(c)


def reverse(nums : list):
    n = len(nums)
    for i in range(n-1, -1, -1):
        yield nums[i]


print(list(reverse([1, 2, 3])))