

#Note: 'Read a book' is a low priority task. Consider completing it when you have free time.
#Reminder: 'Finish project report' is a high priority task that requires immediate attention today!

while True:
    task = input("Enter your task:")
    if task.lower() == "quit":
        break
    Priority = input("Priority (high/medium/low):")
    time_bound = input("Is it time-bound? (yes/no):")
    match time_bound :
        case "yes":
            print(f"Reminder: '{task}' is a {Priority} priority task that requires immediate attention today!")
        case "no":
            print(f"Note: '{task}' is a {Priority} priority task. Consider completing it when you have free time.")