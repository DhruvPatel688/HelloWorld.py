#Text-based Adventure Game: Design a text-based game where the player can make choices that affect the outcome of the story.
import random
class Adventure:
    def __init__(self, player, opponent, lives):
        self.player = player
        self.opponent = opponent
        self.lives = lives
    def level1(self):
        if self.opponent == "Grizzly Bear":
            print("Your opponent is the Grizzly Bear")
            answer = input("""What are you going to do now? You choose:
                  A) Run
                  B) Fight
                  C) Climb up a Tree
                  D) Howl 
                           """)
            if answer == "A" or answer == "B" or answer == "D":
                print("You lose.")
                self.lives -= 1
            elif answer == "C":
                print("You survived to fight another day.")
        elif self.opponent == "Cannibals":
            print("Your opponents are Cannibals")
            answer = input("""What are you going to do now? You choose:
                  A) Run
                  B) Fight
                  C) Climb up a tree
                  D) Howl 
                           """)
            if answer == "C" or answer == "B" or answer == "D":
                print("You lose.")
                self.lives -= 1
            elif answer == "A":
                print("You survived to fight another day.")
        elif self.opponent == "Lion":
            print("Your opponent is the lion")
            answer = input("""What are you going to do now? You choose:
                  A) Run
                  B) Fight
                  C) Eat
                  D) Howl 
                           """)
            if answer == "A" or answer == "B" or answer == "D":
                print("You lose.")
                self.lives -= 1
            elif answer == "C":
                print("You survived to fight another day.")
        elif self.opponent == "Tiger":
            print("Your opponent is the Tiger")
            answer = input("""What are you going to do now? You choose:
                  A) Run
                  B) Fight
                  C) Call Mike Tyson
                  D) Howl 
                           """)
            if answer == "A" or answer == "B" or answer == "D":
                print("You lose.")
                self.lives -= 1
            elif answer == "C":
                print("You survived to fight another day.")
        print(self.lives)


lives = 5
players = ["Cowboy", "Astronaunt", "Navy Seal", "English Teacher"]
print(players)
player = input("Pick a player from the list: ")
opponents = ["Grizzly Bear", "Cannibals", "Lion", "Tiger"]
random_choice = random.choice(opponents)
opponent = random_choice
adventure = Adventure(player, opponent, lives)
adventure.level1()
