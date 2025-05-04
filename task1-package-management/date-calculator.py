from datetime import datetime
def calculate_days_between():
    """
    this code allows the user to enter two dates in 'YYYY-MM-DD' form and it calculates the
    difference between them in days.

    Example:
    Enter the start date (YYYY-MM-DD): 2025-05-01
    Enter the end date (YYYY-MM-DD): 2025-05-04
    Difference in days: 3

    If an invalid date form is entered, an error message will be shown.
    """
    try:
        start = input("Enter the start date (YYYY-MM-DD): ")
        end = input("Enter the end date (YYYY-MM-DD): ")
        d1 = datetime.strptime(start, "%Y-%m-%d")
        d2 = datetime.strptime(end, "%Y-%m-%d")
        difference = abs((d2 - d1).days)
        print("Difference in days:", difference)
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

calculate_days_between()