import random

def main():
    name = input("\nEnter name: ")

    player_score = 0
    cpu_score = 0

    while True:
        choice1 = player_choice()
        choice2 = cpu_choice()

        result, player_score, cpu_score = scoring(
            choice1, choice2, player_score, cpu_score
        )

        display_round(name, choice1, choice2, result)
        display_score(name, player_score, cpu_score)

        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            break


def player_choice():
    while True:
        try:
            print("\nSelect option:")
            print("1. Rock")
            print("2. Paper")
            print("3. Scissors")
            choice = int(input())

            if choice not in range(1, 4):
                print("Please choose from 1-3")
                continue

            return choice

        except ValueError:
            print("Please enter a number (1-3)")


def cpu_choice():
    return random.randint(1, 3)


def scoring(p, c, player_score, cpu_score):
    if p == c:
        return "Draw", player_score, cpu_score

    elif (p == 1 and c == 3) or (p == 2 and c == 1) or (p == 3 and c == 2):
        return "Player wins", player_score + 1, cpu_score

    else:
        return "CPU wins", player_score, cpu_score + 1


def display_round(name, p, c, result):
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    print(f"\n{name} chose {choices[p]}")
    print(f"CPU chose {choices[c]}")
    print(result)


def display_score(name, player_score, cpu_score):
    print(f"\nScore → {name}: {player_score} | CPU: {cpu_score}")


if __name__ == "__main__":
    main()
