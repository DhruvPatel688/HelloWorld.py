def car():
    car = input("Which car would you like to add? ")
    super_cars.append(car)
    print(super_cars)

print("Welcome to the super car garage:")
super_cars = ["Bugatti","Lamborghini", "Ferrari", "Porsche", "Maserati", "Rolls Royce", "Aston Martin"]
for i in super_cars:
    print(i)

index = 1
while index > 0:
    answer = input("Do you have any more cars that you would like to add to your garage? ")
    if answer == "yes":
        car()
    else:
        break

