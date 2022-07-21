import random

with open("wordlist.10000.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
    random_word = random.choice(words).upper()
    while len(random_word) != 5:
        random_word = random.choice(words).upper()
    print(random_word)


def grammar_check(word):
    user_word = str(input()).upper()
    while len(user_word) != 5:
        user_word = str(input("5 characters only: "))
    if not user_word.isalpha():
        user_word = str(input("Only characters: ")).isalpha()
    return user_word


def check(random_word):
    tries = 6
    win = False
    check_word = []
    for i in range(tries):
        check_word = []
        user_word = input("Enter your word: ").upper()
        if user_word == random_word:
            print(f"Your guessed!, it's {random_word}")
            win = True
            exit()
        else:
            for a in range(len(random_word)):
                if user_word[a] == random_word[a]:
                    check_word.append(user_word[a].upper())
                elif user_word[a] in random_word:
                    check_word.append(user_word[a].lower())
                elif user_word[a] != random_word[a]:
                    check_word.append("x")

        print(*check_word)

    if tries > 0:
        print("\nYou're our of tries!")


def start():
    check(random_word)


start()
