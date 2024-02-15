def is_leap(year):
    """
    Returns True if the year is a leap year, False otherwise."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """
    Returns the number of days in a given month in a year."""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]


year = int(input('What year?\n'))
month = int(input('What month?\n'))
days = days_in_month(year, month)
print(days)
