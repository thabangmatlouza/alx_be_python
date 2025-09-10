# Import necessary modules
from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in the format YYYY-MM-DD HH:MM:SS
    """
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))


def calculate_future_date():
    """
    Prompt the user for a number of days, calculate the future date,
    and display it in the format YYYY-MM-DD
    """
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: ").strip())
        future_date = datetime.now() + timedelta(days=days_to_add)
        print("Future date:", future_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid input. Please enter an integer number of days.")


def main():
    display_current_datetime()
    calculate_future_date()


if __name__ == "__main__":
    main()

