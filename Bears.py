class Bear:
    def __init__(self, species, idiot):
        self.species = species
        self.idiot = idiot
    def __repr__(self):
        return f"Bear({self.species})"
    def plan1(self, species, idiot):
        if self.species == "Grizzly Bear":
            print("You are already dead. WTF are you doing in the forest anyway. You are an idiot,", self.idiot)
            answer = input("Pick an option A) Curl up in a ball and wait, B) run, C) shout, D) fight")
            if answer == "A":
                print("You live with a broken back, broken legs, and broken arms. You might bleed to death, but atleast you have a chance.")
            else:
                print(self.idiot, "Death by:", self.species)
        elif self.species == "Black Bear":
            print("You have a small chance for survival if you watched the joe rogan podcast on bears.")
            answer = input("Pick an option A) Look Bigger, B) Fight it, C) Shoot it")
            if answer == "C":
                print("You lived but now the liberals will you sue you for animal cruelty")
            else:
                print("You idiot why didn't you shoot it. You liberal idiot.")
    
bears = {"Grizzly Bear": 6, "Black Bear": 7 }
bear_species = []
print("You are walking through Yellowstone National Park (bear country)")
print(bears)
idiot = input("What is your name?")
species = input("What species did you encounter?")
bear = Bear(species, idiot)
print(repr(bear))
bear.plan1(species, idiot)

