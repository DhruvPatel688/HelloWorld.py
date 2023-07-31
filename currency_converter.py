currencies = {"euro": 0.91, "peso": 16.73, "pounds": 0.78, "yen": 142.15, "yuan": 7.14}
for key in currencies.keys():
    print(key)
while True:
    answer = input("Which currency would you like to convert to? ")
    try:
        if answer in currencies:
            break
        else:
            print("Please enter a currency from the options.")
    except ValueError:
        print("Invalid input. Please enter a valid option.")
while True:
    dollar = float(input("How many dollars do you want to convert? "))
    try:
        number = dollar
        if number > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

money  = currencies[answer] * dollar
print(money)
