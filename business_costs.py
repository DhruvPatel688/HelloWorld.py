fixed_costs = {}
variable_costs = {}

def costs():
    index = int(input("How many fixed costs do you have?"))
    while index > 0:
        a = input("What is one of your fixed costs? ")
        b = float(input("How much is it? "))
        fixed_costs[a] = b
        index -= 1
    print("Your fixed costs are: ",fixed_costs)
    cost = sum(value for value in fixed_costs.values())
    print("The total fixed cost is ",cost)
    index = int(input("How many variable costs do you have?"))
    while index > 0:
        a = input("What is one of your variable costs? ")
        b = float(input("How much is it? "))
        variable_costs[a] = b
        index -= 1
    print("Your variable costs are: ",variable_costs)
    variable_cost = sum(value for value in variable_costs.values())
    print("The total variable cost is ",variable_cost)
    combined_cost = cost + variable_cost
    print("Your total company costs are ", cost + variable_cost)
    combined_costs = {**fixed_costs, **variable_costs}
    print(combined_costs)

def revenue():
    goal = int(input("How much money do you want to make in revenue? "))
    product_price = int(input("What is the price of your product or service?"))
    margin = goal / product_price
    print("You must sell ", margin, "products or services to meet your goal of", goal)

costs()
revenue()
