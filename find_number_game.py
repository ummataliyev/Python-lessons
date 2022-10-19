import random


def find_number(x=10):
    random_number = random.randint(1, x)
    print(f"I thought of a number from 1 to {x}. Can you find it?", end="")
    assumoptions = 0
    while True:
        assumoptions += 1
        assumoption = int(input(">>>"))
        if assumoption < random_number:
            print("Say a bigger number:", end="")
        elif assumoption > random_number:
            print("Say a smaller number:", end="")
        else:
            print("You won!")
            break

    print(f"Congratulations you found it with {assumoptions} guesses!")
    return assumoptions


def find_number_pc(x=10):
    input(f"Think of a number from 1 to {x} and press any button. I will find.")
    low = 1
    high = x
    assumoptions = 0
    while True:
        assumoptions += 1
        if low != high:
            assumoption = random.randint(low, high)
        else:
            assumoption = low
        answer = input(
            f"You guessed the number {assumoption}: true (T),"
            f"Press (+) if the number I think is bigger than that, or (-) if lower".lower()
        )
        if answer == "-":
            high = assumoption - 1
        elif answer == "+":
            low = assumoption + 1
        else:
            break
    print(f"I found with {assumoptions} guesses!")
    return assumoptions


def play(x=10):
    again = True
    while again:
        assumptions_pc = find_number_pc(x)
        assumptions_user = find_number(x)

        if assumptions_user > assumptions_pc:
            print(f"I found with {assumptions_pc} guesses. I won!")
        elif assumptions_user < assumptions_pc:
            print(f"You found with {assumptions_user} guesses. You won!")
        else:
            print("Draw!")
        yana = int(input("Will we play again? YES(1)/NO(0):"))


play()
