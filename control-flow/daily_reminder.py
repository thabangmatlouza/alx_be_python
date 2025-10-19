task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is high priority task that requires immediate attention today! ")
        else:    
            print(f"Reminder: {task} is low priority. Consider completing it when you have free time. ")   

    case _:
        print("Unexpected input. ")
