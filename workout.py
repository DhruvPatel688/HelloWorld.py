Chest = ["dumbbell press", "cross press"]
Arms = [ ["Pick one bicep: dumbbell curl, cross body curl, vertical curl"], ["Pick one forearm: horizatonal flex, curled downs, banded flex"], ["shoulder variations: lateral raises, front lateral raises, overhead press"], ["tricep variations: dumbbell press, banded pull downs, pushups"]]
Abs = ["Pull up bar leg crunches", "flutter kicks"]
Back = ["Pull ups"]
Legs = ["Weighted Squats", "Weighted lunges", "calve lifts"]
monday = [Chest, Arms, Abs]

tuesday = [Legs, Back, Arms, Abs]

wednesday = [Chest, Legs, Arms, Abs]

thursday = monday

friday = tuesday

saturday = wednesday

sunday = friday 

special = {"Weighted Burpees overhead": 25, "high jumps": 25, "Squat plus overhead": 25, "traps and tricep grip and overhead": 25}

def iterate(list):
    for i in list:
        print(i)
print("Welcome to your workout guide")
def day():
    day = input("What day is it?")
    print("All workouts will be completed in 3 sets and 12 reps.")
    if day == "monday":
        print("Your morning workout today is:")
        print(["Chest", "Arms", "Abs"])
        iterate(monday)
    elif day == "tuesday":
        print("Your morning workout today is:")
        print(["Legs", "Back", "Arms", "Abs"])
        iterate(tuesday)
    elif day == "wednesday":
        print("Your morning workout today is:")
        print(["Chest", "Legs", "Arms", "Abs"])
        iterate(wednesday)
    elif day == "thursday":
        print("Your morning workout today is:")
        print(["Chest", "Arms", "Abs"])
        iterate(thursday)
    elif day == "friday":
        print("Your morning workout today is:")
        print(["Legs", "Back", "Arms", "Abs"])
        iterate(friday)
    elif day == "saturday":
        print("Your morning workout today is:")
        print(["Chest", "Legs", "Arms", "Abs"])
        iterate(saturday)
    elif day == "sunday":
        print("Your morning workout today is:")
        print(["Legs", "Back", "Arms", "Abs"])
        iterate(sunday)
    print("Your afternoon workout is:")
    print(special)
      
day()
