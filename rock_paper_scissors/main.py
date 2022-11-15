import drawings_rock_paper_scissors
import random

d_list = [drawings_rock_paper_scissors.rock, drawings_rock_paper_scissors.paper,
          drawings_rock_paper_scissors.scissors]
your_wins = cp_wins = 0
print("Welcome to the rock, paper or scissors game. The first player to reach 3 points wins the game!\n")

while (your_wins < 3) and (cp_wins < 3):
    choice = input("Press '1' for rock, '2' for paper and '3' for scissors!\n")
    if choice != '1' and choice != '2' and choice != '3':
        print("Please type a valid choice!\n")
    else:
        choice = int(choice)
        cp_choice = random.randint(1, 3)
        print("Your choice:\n")
        print(d_list[choice - 1])
        print("Computer choice:\n")
        print(d_list[cp_choice - 1])
        if choice == cp_choice:
            print("It's a draw.\n")
        elif (choice == 1 and cp_choice == 3) or (choice == 2 and cp_choice == 1) or (choice == 3 and cp_choice == 2):
            print("You win!\n")
            your_wins += 1
        else:
            print("You lose.\n")
            cp_wins += 1
    print(f"Your score is {your_wins}\n")
    print(f"Computer score is {cp_wins}\n")

if your_wins == 3:
    print("Congratulations, you won the game!")
else:
    print("Unfortunately, you lost the game.")
