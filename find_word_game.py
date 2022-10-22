import random
from uzwords import words


def get_word():
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()


def display(entered_letter, word):
    display_letter = ""
    for letter in word:
        if letter in entered_letter:
            display_letter += letter
        else:
            display_letter += "-"
    return display_letter


def play():
    word = get_word()
    word_letters = set(word)
    entered_letter = ""
    print(f"Мен {len(word)} хонали сўз ўйладим. Топа оласизми?")
    # print(word)
    while word_letters:
        print(display(entered_letter, word))
        if entered_letter:
            print(f"Шу вақтгача топган ҳарфларингиз: {entered_letter}")

        letter = input("Ҳарф киритинг: ").upper()
        if letter in entered_letter:
            print("Бу ҳарфни аввал киритгансиз. Бошқа ҳарф киритинг.")
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f"{letter} ҳарфи тўғри.")
        else:
            print("Бундай ҳарф йўқ.")
        entered_letter += letter
    print(f"Табриклайман! {word} сўзини {len(entered_letter)} та уринишда топдингиз.")


play()