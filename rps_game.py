import random

def main():
    name = input("\nEnter name: ")
    
    choice1 = player_choice(choice1)
    choice2 = cpu_choice(choice2)
    player_score, cpu_score = scoring(choice1, choice2)
def player_choice(choice1):
    try:
        while True:
            print("\nSelect option:\n")
            print("1. Rock")
            print("2. Paper")
            print("3. Scissors")
            choice1 = int(input())
            
            if choice1 not in range(1, 3):
                print("Please choose from 1-3")
                continue
            else:
                return choice1
            
    except ValueError:
        print("Please enter an integer (1-3)")
    except Exception as e:
            print(f"An unexpected error occurred: {e}\n")
            
def cpu_choice(choice2):
    choice2 = random.randint(1, 3)
    return choice2

def scoring(choice1, choice2):
    if choice1 == 1 and choice2 == 1:
        player_score += 0
        cpu_score += 0 
    elif choice1 == 1 and choice2 == 2:
        player_score += 0
        cpu_score += 1
        
#Yeah ts isn't working. I'm taking a break