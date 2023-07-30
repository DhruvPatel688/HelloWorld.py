# This calculator converts temperature from celsius to faherhiet and vice versa.
class Temperature:
    def __init__ (self, number):
        self.number = number
    def fahrenheit(self):
        answer = (self.number * (9/5)) + 32
        print(self.number, "celsius is ", answer, " degrees fahrenhiet.")
    def celsius(self):
        answer = (self.number * (5/9)) - 32
        print(self.number, "fahrenhiet is ", answer, " degrees celsius.")

print("Welcome to the temperature conversion calculator.")
temp = str(input("What temperature do you want to convert to? Type the letter: A)Fahrenheit or  B)Celsius "))
temp_lower = temp.lower()
number = float(input("What is the number? "))
temperature = Temperature(number)
if temp_lower == "a":
    temperature.fahrenheit()
elif temp_lower == "b":
    temperature.celsius()
else:
    print("You did not type A or B, run the program again.")
