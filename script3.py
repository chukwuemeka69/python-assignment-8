#! /usr/bin/python3


from datetime import datetime

def days_between_dates(date1_str, date2_str, date_format="%Y-%m-%d"):

    """
    Calculate the number of days between two dates.

    Parameters:
     - date1_str, date2_str: The input dates as strings.
     - date_format: The format of the input dates. Default is YYYY-MM-DD.
    Returns:
     - Number of days between date1 and date2.
 """

    date1 = datetime.strptime(date1_str, date_format)
    date2 = datetime.strptime(date2_str, date_format)

    return abs((date2 - date1).days)

if __name__ == "__main__":
    # Prompt the user for input dates
    date1_str = input("Enter the first date (format: YYYY-MM-DD): ")
    date2_str = input("Enter the second date (format: YYYY-MM-DD): ")

    # Calculate and print the number of days
    days = days_between_dates(date1_str, date2_str)
    print(f"The number of days between {date1_str} and {date2_str} is {days} days.")
