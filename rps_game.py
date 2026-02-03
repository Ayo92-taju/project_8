import random

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        
    def choose(self):
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
        
class CPU:
    def __init__(self):
        self.score = 0
        
    def choose(self):
        return random.randint(1, 3)
        
class Game:
    def __init__(self):
        name = input("\nEnter name: ")
        self.player = Player(name)
        self.cpu = CPU()
        self.choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    
    def play(self):
        p_choice = self.player.choose()
        c_choice = self.cpu.choose()
        
        print(f"{self.player.name} chose {self.choices[p_choice]}")
        print(f"CPU chose {self.choices[c_choice]}")
        if p_choice == c_choice:
            print("Draw")

        elif (p_choice == 1 and c_choice == 3) or (p_choice == 2 and c_choice == 1) or (p_choice == 3 and c_choice == 2):
            self.player.score += 1
            print(f"{self.player.name} wins")

        else:
            self.cpu.score += 1
            print("CPU wins")
    
    def displayScore(self):
        print("\nScores:")
        print(f"{self.player.name}: {self.player.score}")
        print(f"CPU: {self.cpu.score}")
        
    def main(self):
        while True:
            self.play()
            self.displayScore()
            
            again = input("\nDo you want to play another round? (y/n)").lower()
            if again != "y":
                break


if __name__ == "__main__":
    app = Game()
    app.main()