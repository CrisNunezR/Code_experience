"""
In a file called seasons.py, implement a program that prompts
the user for their date of birth in YYYY-MM-DD format and then
sings prints how old they are in minutes, rounded to the nearest
integer, using English words instead of numerals, just like the
song from Rent, without any and between words.

Since a user might not know the time at which they were born, assume,
for simplicity, that the user was born at midnight (i.e., 00:00:00)
on that date. And assume that the current time is also midnight.
In other words, even if the user runs the program at noon, assume
that it’s actually midnight, on the same date. Use datetime.date.today
to get today’s date, per docs.python.org/3/library/datetime.html#datetime.date.today.
"""


from datetime import date
import sys
import re
import inflect

def main():
    while True:
        str_ = input("Date of Birth: ").strip()

        if len(str_) == 10:
            try:
                year, month, day = get_date(str_)
            except ValueError:
                sys.exit('Invalid date')

            else:
                today_midnight = date.today()
                minutes_number = int(calculate_minutes(year, month, day, today_midnight))
                minutes = number_to_words(minutes_number)
                print(f"{minutes} minutes")
                break
        else:
            sys.exit('Invalid date')

#receives a str date and extracts year, month and day as strings
def get_date(date):
        if _date := re.search(r"^([12][09][0-9][0-9])\-([0][1-9]|1[0-2])\-([0][1-9]|[12][0-9]|3[01])$", date):
            year = _date.group(1)
            month = _date.group(2)
            day = _date.group(3)
            if 1 > int(month) > 12:
                raise ValueError("Month must be a value between 01 and 12")
            if month in ['01','03', '05', '07', '08', '10', '12'] and int(day) > 31:
                raise ValueError("Days must be at most 31")
            if month in ['04','06', '09', '11'] and int(day) > 30:
                raise ValueError("Days must be at most 30")
            if month == '02' and int(day) > 29:
                raise ValueError("Days must be at most 29")

            #print(year, month, day)
        else:
            raise ValueError("Invalid date")

        return year, month, day

#receives a 2 dates and calculates the minute difference
def calculate_minutes(year, month, day, today_midnight):
    input_date = date(int(year), int(month), int(day))

    #calculate time difference
    time_difference = today_midnight - input_date
    minute_difference = time_difference.total_seconds()/60

    return minute_difference

def number_to_words(minutes: int):
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")
    words = words[0].upper() + words[1:]
    return words

if __name__ == "__main__":
    main()