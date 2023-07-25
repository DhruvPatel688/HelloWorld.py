product = float(input("What is the product price? "))
percentage = float(input("What percentage commission do you recieve per sale? "))
goal = float(input("What is your goal in revenue by the end of the year? "))
profit_per_capita = product * (percentage / 100)
sales = goal / profit_per_capita
print("Your goal in sales should be ", sales, "in order to reach", goal)
print("You would make ", profit_per_capita, "per sale.")
# End of the sales goal aspect of code

# Start for the time spenduture sequence
percent_success = (float(input("What percent of your cold calls lead to a close? Default is 0.2 ")) / 100)
number = sales / percent_success
print("Based on percent success, you must do ", number, " cold calls")
employees = int(input("How many employees do you have? "))
if employees == 0:
    per_day = number / 365
    print("You must make ", per_day, " cold calls a day.")
    time = (per_day / 10)
    print("You must work ", time, "hours per day to achieve the goal.")
else:
    per_day = (number / 365) / (employees + 1)
    print("You must make and your employees each must make ", per_day, " cold calls a day.")
    time  = (per_day / 10)
    print("Each employee must work ", time, "hours per day to achieve the goal.")

# Realistic approach:

hours = float(input("How many hours can you work a day? "))
calls = hours *10
year = 365 * calls
percent_success = year * 0.002
money = profit_per_capita * percent_success
print("You would make ", calls, "calls a day, ", year, "calls a year, and you would make ", money, "dollars per year.")
