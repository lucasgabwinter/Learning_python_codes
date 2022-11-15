import random
import hangman_art


print(hangman_art.logo)
chosen_word = random.choice(hangman_art.word_list)
lives = 6
win = False
blank_list = []
user_choices = []
for letter in chosen_word:
    blank_list.append("_")

while lives > 0 and not win:
    print("\n")
    print(blank_list)
    guess = input("Guess a letter!\n").lower()
    while len(guess) > 1 or guess in user_choices:
        if len(guess) > 1:
            print("Please type just one character.")
            print("\n")
            print(blank_list)
            guess = input("Guess a letter!\n").lower()
            print(blank_list)
        if guess in user_choices:
            print("This character was already chosen.")
            print("Remember your previous choices:")
            print(user_choices)
            print("\n")
            print(blank_list)
            guess = input("Guess a letter!\n").lower()
    user_choices.append(guess)
    aux = 0
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            blank_list[position] = letter
            aux = 1
    if aux == 0:
        print("Wrong choice.")
        lives -= 1
        print(hangman_art.stages[lives])
        print(f"You have {lives} lives left.")
    else:
        print("Correct!")

    if "_" not in blank_list:
        win = True
    else:
        if lives > 0:
            print("Remember your previous choices:")
            print(user_choices)

if win:
    print(blank_list)
    print("Congratulations, you beat the game!")
else:
    print(blank_list)
    print("You lost.")
    print(f"The secret word was {chosen_word}.")
