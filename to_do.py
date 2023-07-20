to_do = {}
done = {}

def lists(tasks):
    for task, task_number in tasks.items():
        print("Task Number", task_number, "is:", task)

def sort(tasks):
    answer = input("If you have completed a task type 'completed', if not type 'not completed': ")
    if answer == "completed":
        answer2 = input("Which task have you completed? ")
        if answer2 in tasks:
            done[answer2] = tasks[answer2]
            del tasks[answer2]
            print("You still have to complete:")
            lists(tasks)
        else:
            print("Task is not in the list.")
    elif answer == "not completed":
        if len(tasks) == 0:
            print("You have completed all tasks!")
        else:
            print("Tasks left to complete:")
            lists(tasks)

def get_info():
    numbers = int(input("Hello, This is your to-do list task manager. How many tasks would you like to accomplish? "))
    index = 1

    while numbers > 0:
        print("Task number", index, "is")
        item = input("Type here: ")
        to_do[item] = index
        numbers -= 1
        index += 1


def execute_code():
    get_info()
    print("The items in your to-do list are below.")
    lists(to_do)
    while len(to_do) > 0:
        sort(to_do)

def iterate_it():
    execute_code()
    yes_no = input("Do you have any more tasks you want to add? (yes/no): ")
    if yes_no.lower() == "yes":
        iterate_it()

iterate_it()
