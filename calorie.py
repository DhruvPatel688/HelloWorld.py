meals = []
def balanced_diet(calories):
    carbs = .60 * calories / 4
    protein = .25 * calories / 4
    fats = .15 * calories / 9
    print("Your daily macros in grams are", carbs, "of carbs", protein, "of protien", fats, "of fat.")
    while calories > 0:
        print("Lets track your calories:")
        print("What did you eat ?")
        meal = input()
        meals.append(meal)
        print("How many calories was it?")
        caloric = float(input())
        meals.append(caloric)
        print("How many grams of protein, carbs, and fats(enter each number on separate line)?")
        pro = float(input())
        car = float(input())
        fa = float(input())
        protein -= pro
        carbs -= car
        fats -= fa
        calories -= caloric
        if calories > 0:
            print("You still need to eat", calories," calories.")
        else:
            print("You should stop eating")
        if protein > 0:
            print("You still need to eat", protein," protein.")
        else:
            print("You should stop eating protein")
        if carbs > 0:
            print("You still need to eat", carbs," carbs.")
        else:
            print("You should stop eating carbs")
        if fats > 0:
            print("You still need to eat", fats," fats.")
        else:
            print("You should stop eating fats")
        
        


def maintain(weight):
    calories = float(weight) * 14
    print("Your maintance calories are:",calories)
    print(balanced_diet(calories))
def calorie_intake_heavy_bulk(weight):
    calories  = float(weight) * 21
    print("Your heavy bulk calories are:", calories)
    print(balanced_diet(calories))
def calorie_intake_light_bulk(weight):
    calories = float(weight) * 17
    print("Your light bulk calories are:", calories)
    print(balanced_diet(calories))
def calorie_intake_light_cut(weight): 
    calories = float(weight) * 11
    print("Your light cut calories are:", calories)
    print(balanced_diet(calories))
def calorie_intake_heavy_cut(weight): 
    calories  = float(weight) * 7
    print("Your heavy cut calories are:", calories)
    print(balanced_diet(calories))
print("Calorie guide")
name = input("Enter your name: ")
print("Hello,", name, ". This is your customizable guide to getting in shape. If your ready, lets get started.")
print("Enter your weight in pounds")
weight = input()
print("Do you want to bulk, cut, or maintain?")
answer = input()
options = ["maintain", "light bulk", "heavy bulk", "light cut", "heavy cut"]
if answer == "maintain":
    maintain(weight)
elif answer == "bulk":
    print(options[1:3])
    print("Do you want to heavy bulk or light bulk?")
    answer = input()
    if answer == "light bulk":
        calorie_intake_light_bulk(weight)
    elif answer == "heavy bulk":
        calorie_intake_heavy_bulk(weight)
elif answer == "cut":
    print(options[3:5])
    print("Do you want to heavy cut or light cut?")
    answer = input()
    if answer == "light bulk":
        calorie_intake_light_cut(weight)
    elif answer == "heavy bulk":
        calorie_intake_heavy_cut(weight)
