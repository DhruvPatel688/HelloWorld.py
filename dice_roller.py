import random


print("This is a dice rolling simulator. You will roll two dice and the results will be displayed.")
answer = input("Would you like to roll dice? Enter yes or no: ")
if answer != "yes" and answer != "no":
    print("You did not write yes or no. Try again")
while answer == "yes":
    print("The first dice is", random.randint(1, 6), "and the second is", random.randint(1, 6))
    answer = input("Would you like to roll again? Enter yes or no: ")
    if answer != "yes" and answer != "no":
        print("You did not write yes or no. Try again")
