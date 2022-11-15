import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_wins = 0
dealer_wins = 0


def check_aces(player_cards_):
    count = 0
    for card in player_cards_:
        if card == 11:
            player_cards_[count] = 1
            return player_cards_
        count += 1
    return player_cards_


def print_only_dealer_score(d_cards, d_score):
    print("Dealer cards")
    print(d_cards)
    print("Dealer score")
    print(d_score)


def print_only_player_score(u_cards, u_score, d_cards):
    print("Your cards.")
    print(u_cards)
    print("Your current score.")
    print(u_score)
    print("Dealer first card")
    print(d_cards[0])


def check_valid(answer):
    if answer == "yes":
        return "yes"
    if answer == "no":
        return "no"
    else:
        print("Wrong response!")
        answer = check_valid(input("Type 'yes' for yes or 'no' for no!\n"))
        return answer


def calc_score(cards_):
    score = 0
    for card in cards_:
        score += card
    return score


continue_game = True
while continue_game:
    user_score = 0
    dealer_score = 0
    user_cards = []
    dealer_cards = []

    continue_turn = True
    while continue_turn:
        user_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))
        user_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))
        user_score = calc_score(user_cards)
        dealer_score = calc_score(dealer_cards)

        if user_score > 21:
            user_cards = check_aces(user_cards)
            user_score = calc_score(user_cards)
        if dealer_score > 21:
            dealer_cards = check_aces(dealer_cards)
            dealer_score = calc_score(dealer_cards)

        print_only_player_score(user_cards, user_score, dealer_cards)

        if dealer_score == 21:
            dealer_wins += 1
            print("Dealer won the turn with a BlackJack.")
            break
        elif user_score == 21:
            user_wins += 1
            print("You won the turn with a BlackJack!")
            break

        user_game = True
        while user_score < 21 and user_game:
            draw_card = check_valid(input("Do you want to draw another card? "
                                          "Type 'yes' or 'no'!\n"))
            if draw_card == "yes":
                user_cards.append(random.choice(cards))
                user_score = calc_score(user_cards)
                if user_score > 21:
                    user_cards = check_aces(user_cards)
                    user_score = calc_score(user_cards)
                print_only_player_score(user_cards, user_score, dealer_cards)
            else:
                user_game = False
        if user_score > 21:
            print("You lose.")
            dealer_wins += 1
            continue_turn = False
        else:
            dealer_game = True
            while dealer_score < 17:
                dealer_cards.append(random.choice(cards))
                dealer_score = calc_score(dealer_cards)
                if dealer_score > 21:
                    dealer_cards = check_aces(dealer_cards)
                    dealer_score = calc_score(dealer_cards)
            if dealer_score > 21 or dealer_score < user_score:
                print_only_dealer_score(dealer_cards, dealer_score)
                print("You win!")
                user_wins += 1
                continue_turn = False
            elif dealer_score == user_score:
                print_only_dealer_score(dealer_cards, dealer_score)
                print("It's a draw.")
                continue_turn = False
            else:
                print_only_dealer_score(dealer_cards, dealer_score)
                print("You lose.")
                dealer_wins += 1
                continue_turn = False
    print(f"Main score: Player: {user_wins} wins. Dealer: {dealer_wins} wins.")
    answer_continue = check_valid(input("Do you want to play another turn? Type"
                                        " 'yes' or 'no'!\n"))
    if answer_continue == "no":
        continue_game = False
    else:
        continue_turn = False


print("Player total wins:")
print(user_wins)
print("Dealer total wins:")
print(dealer_wins)
if user_wins > dealer_wins:
    print("You won the game!")
elif dealer_wins > user_wins:
    print("You lost the game.")
else:
    print("The game ended in a draw.")
