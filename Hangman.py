import os
import random
import socket
import urllib.request


hang_man = ["""
        +---+
        |   |
        |
        |
        |
        |
        |
    ===========
            \n""",
            """
        +---+
        |   |
        |   O
        |
        |
        |
        |
    ===========\n""",
            """
        +---+
        |   |
        |   O
        |   |
        |   |
        |
        |
    ===========\n""",
            """
        +---+
        |   |
        |   O
        |  /|
        |   |
        |
        |
    ===========\n""",
            """
        +---+
        |   |
        |   O
        |  /|\\
        |   |
        |
        |
    ===========\n""",
            """
        +---+
        |   |
        |   O
        |  /|\\
        |   |
        |  /
        |
    ===========\n""",
            """
        +---+
        |   |
        |   O
        |  /|\\
        |   |
        |  / \\
        |
    ==========="""]

os.system("cls")

url = "https://pastebin.com/raw/RnDPnp9V"
# word_list = ["Super", "Colourful", "Appetite"]
with urllib.request.urlopen(url) as response:
    data = response.readlines()
# data = data.splitlines()
# response = urllib.request.urlopen(url)
# data = response.splitlines()
# text = data.decode("utf-8")
# f = open(url, "r").splitlines()
# word_list = f.readlines()
random_word = random.choice(data)
random_word_lower = random_word.lower().decode("utf-8").strip()
# randdom_word_lower = random_word_lower.decode("utf-8").strip()
# word_list.close()

guesses = 0
guessed_letters = []
correct_guesses = []
masked_word = []
word_dict = {}

output = ["_"] * len(random_word_lower)

def print_output():
    print(''.join([x + " " for x in output]))


while guesses < 6:

    print("=" * 50)
    print(hang_man[guesses])
    print_output()

    print("\n\nGuessed letters:", guessed_letters, end=" ")
    print("\n\nGuess the letter >", end=" ")
    guessed_letter = input()

    if len(guessed_letter) != 1:
        print("One letter needs to be guessed")
        continue

    if guessed_letter in guessed_letters:
        print("\nAlready guessed that letter. Try something else...")
        continue

    guessed_letters.append(guessed_letter)

    if guessed_letter not in random_word_lower:
        guesses += 1

        if guesses > 5:
            os.system("cls")
            print(hang_man[guesses], end="\n\n")
            print(guessed_letters)
            print("\nThe correct word was", random_word_lower, end="\n\n\n")

    else:
        guessed_letter_index = [i for i, e in enumerate(random_word_lower) if e == guessed_letter]

        for i in guessed_letter_index:
            masked_word.append(random_word_lower[i])
            correct_guesses.append(guessed_letter)
            word_dict[i] = random_word_lower[i]

        for i,x in enumerate(random_word_lower):
            if x is guessed_letter:
                output[i] = guessed_letter

        if len(correct_guesses) == len(random_word_lower):
            os.system("cls")
            print(hang_man[guesses], end="\n")
            print("\nCONGRATULATIONS! \n\nYou win!!")
            print("\nThe word was", random_word_lower.upper(), end="\n\n\n")

            # again = input("\nDo you want to play again? (yes/no) ")
            # if again.startswith("y"):
            #     main()
            # else:
            break

# if __name__ == "__main__":
# main()