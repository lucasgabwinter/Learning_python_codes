import random


def print_results(first, second):
    print(f"{first['name']} has a total of "
          f"{first['follower_count']} millions of followers and\n"
          f"{second['name']} has a total of "
          f"{second['follower_count']} millions of followers!")


def check_valid(answer_, p1, p2):
    if answer_ == p1:
        return answer_
    if answer_ == p2:
        return answer_
    else:
        print("Wrong response!")
        answer_ = check_valid(input("Please type a valid answer.\n"), p1, p2)
        return answer_


def new_try():
    continue_ = input("Want to play again? Type 'yes' or 'no'\n")
    continue_ = check_valid(continue_, "yes", "no")
    if continue_ == "yes":
        play()
    else:
        print("Bye bye.")


def play():
    from compare_game_data import data
    print("Welcome to the compare followers game!")
    chosen_people_list = []
    count = 1
    score = 0
    chosen_people1 = random.choice(data)
    chosen_people_list.append(chosen_people1)
    data.remove(chosen_people1)
    game = True

    while game:
        chosen_people2 = random.choice(data)
        chosen_people_list.append(chosen_people2)
        data.remove(chosen_people2)
        print(f"Compare A: {chosen_people_list[count-1]['name']} a"
              f" {chosen_people_list[count-1]['description']}"
              f" from {chosen_people_list[count-1]['country']}")
        print(f"Against B: {chosen_people_list[count]['name']} a"
              f" {chosen_people_list[count]['description']}"
              f" from {chosen_people_list[count]['country']}")
        guess = input("Who has more followers? Type 'a' or 'b'\n")
        guess = check_valid(guess, "a", "b")

        if guess == "a" and chosen_people_list[count-1]["follower_count"] <= chosen_people_list[count]["follower_count"]:
            print("Wrong answer.")
            print_results(chosen_people_list[count - 1], chosen_people_list[count])
            print(f"Game over! Total score: {score}")
            game = False
            new_try()
        elif guess == "b" and chosen_people_list[count-1]["follower_count"] >= chosen_people_list[count]["follower_count"]:
            print("Wrong answer.")
            print_results(chosen_people_list[count - 1], chosen_people_list[count])
            print(f"Game over! Total score: {score}")
            game = False
            new_try()
        elif chosen_people_list[count-1]["follower_count"] == chosen_people_list[count]["follower_count"]:
            print(f"Both have the same amount of followers: {chosen_people_list[count-1]['follower_count']}")
            score += 1
        else:
            score += 1
            print("Correct!")
            print_results(chosen_people_list[count-1], chosen_people_list[count])
            print(f"Total score: {score}")
            count += 1


play()
