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


from datetime import datetime, timedelta
import sys
import re
import inflect

def main():
    birth = Date.get_date()
    print(birth)

#validate date format YYYY-MM-DD
class Date:
    def __init__(self, year=None, month=None, day=None, minute_difference=None):
        self.year = year
        self.month = month
        self.day = day
        self.minute_difference = minute_difference

    #defines the number of minutes
    def calculate_minutes(self):

        today_midnight = datetime.combine(datetime.today(), datetime.min.time())
        #print(today_midnight)
        input_date = datetime(int(self.year), int(self.month), int(self.day))

        #calculate time difference
        time_difference = today_midnight - input_date
        self.minute_difference = time_difference.total_seconds()/60
        #print(self.minute_difference)

    #prints the number of minutes
    def __str__(self):
        p = inflect.engine()
        word = p.number_to_words(int(self.minute_difference), andword="")

        #return f"{self.year} - {self.month} - {self.day}, minutes: {self.minute_difference}"
        return f"{word} minutes"

    #notice that date.fromisoformat(date_string) can also return YYYY-MM-DD with more ease
    @classmethod
    def get_date(cls):
        date = input("Date of Birth: ").strip()
        if not date:
            raise ValueError("Enter a date")
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
            raise ValueError("Invalid date format. Enter YYYY-MM-DD")

        _Date = cls(year, month, day)
        _Date.calculate_minutes() #include minutes

        return _Date

if __name__ == "__main__":
    main()