class Weight:
    def __init__(self, pounds, feet, inches):
        self.pounds = pounds
        self.feet = feet
        self.inches = inches
    def bmi(self):
        height = (self.feet * 12) + self.inches
        answer = (self.pounds/(height**2)) * 703
        print(round(answer, 2))


print("Welcome to the Body Mass Index calculator:")
#pounds = input("What is your weight in pounds? ")

while True:
    pounds = float(input("What is your weight in pounds? "))
    feet = float(input("How many feet tall are you? If you are 5ft 6in, write 5: "))
    inches = float(input("How more inches taller are you? If you are 5ft 6in, write 6: "))
    try:
    
        if pounds > 0 and feet > 0 and inches >= 0:
            break
        else:
            print("Please enter a positive integer.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

weight = Weight(pounds, feet, inches)
weight.bmi()
