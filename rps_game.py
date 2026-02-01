import random

def main():
    name = input("\nEnter name: ")
    
    scores = []
    choice1 = player_choice()
    choice2 = cpu_choice()
    scoring(choice1, choice2, scores)
    display_score(name, scores)
    
def player_choice():
    try:
        while True:
            print("\nSelect option:\n")
            print("1. Rock")
            print("2. Paper")
            print("3. Scissors")
            choice = int(input())
            
            if choice not in range(1, 3):
                print("Please choose from 1-3")
                continue
            else:
                return choice
            
    except ValueError:
        print("Please enter an integer (1-3)")
    except Exception as e:
            print(f"An unexpected error occurred: {e}\n")
            
def cpu_choice():
    choice = random.randint(1, 3)
    return choice

def scoring(choice1, choice2, scores):
    score = {"Player": player_score, "CPU": cpu_score}
    if choice1 == choice2:
        player_score += 0
        cpu_score += 0 
    
    elif (choice1 == 1 and choice2 == 2) or (choice1 == 2 and choice2 == 3) or (choice1 == 3 and choice2 == 1):
        player_score += 0
        cpu_score += 1
    
    elif (choice2 == 1 and choice1 == 2) or (choice2 == 2 and choice1 == 3) or (choice2 == 3 and choice1 == 1):
        player_score += 1
        cpu_score += 0
        
    return scores.append(score)

def display_score(name, scores):
    for i, score in enumerate(scores, start = 1):
                print(f"{name}: {scores["Player"]} | CPU: {scores["CPU"]}")
    

if __name__ == "__main__":
    main()