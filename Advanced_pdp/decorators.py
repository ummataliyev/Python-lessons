# Decorators
import time


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def do():

    time.sleep(3)
    print("do1 is done")


def do2():

    time.sleep(2)
    print("do2 is done")


def timer(func):
    started = time.time()
    func()
    finished = time.time()
    print(f"took {finished - started} seconds")


# timer(do)
# timer(do2)


def star(func):
    def inner():
        print("*" * 12)
        func()
        print("*" * 12)
    return inner

@star
def hello():
    print("Hello world")


hello()