import random

with open("wordlist.10000.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
    random_word = random.choice(words).upper()
    while len(random_word) != 5:
        random_word = random.choice(words).upper()


def grammar_check(word):
    user_word = word
    while len(user_word) != 5:
        user_word = str(input("5 characters only!\nTry again "))
    if not user_word.isalpha():
        user_word = str(input("No digits\nTry again: ")).isalpha()
    if word in words:
        print("success")
    return user_word


def check(random_word):
    tries = 6
    for i in range(tries):
        check_word = []
        user_word = input(F"{i+1}/6 tries. Enter your word: ").upper()
        temp_word = grammar_check(user_word)
        user_word = temp_word
        if user_word == random_word:
            print(f"\nYour guessed, it's {random_word}")
            exit()
        else:
            for a in range(len(random_word)):
                if user_word[a] == random_word[a]:
                    check_word.append(user_word[a].upper())
                elif user_word[a] in random_word:
                    check_word.append(user_word[a].lower())
                elif user_word[a] != random_word[a]:
                    check_word.append("x")

        print(*check_word, sep="|")

    if tries > 0:
        print("\nYou're our of tries!")


def main():
    check(random_word)

if __name__ == "__main__":
    main()