"""


In a file called outdated.py, implement a program that prompts
the user for a date, anno Domini, in month-day-year order,
formatted like 9/8/1636 or September 8, 1636

Then output that same date in YYYY-MM-DD format.
If the user’s input is not a valid date in either
format, prompt the user again. Assume that every month
has no more than 31 days; no need to validate whether
a month has 28, 29, 30, or 31 days.

"""

#function to return format MM or DD
def nn_format(n: int) -> str:
    if 0 < n < 10:
        return "0" + str(n)
    else:
        return str(n)

#function to return day, month and year
def read_date(date: str):

    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

    #identify format by looking at '/' character
    if date.find("/") > -1:

        #read month
        try:
            month = int(date[:date.find("/")])
        except:
            #print("Error in month format")
            pass
        else:
            if month > 12:
                raise ValueError("Invalid month value")

        #ready day
        try:
            day = int(date[date.find("/") + 1: date.find("/") + 1 + date[date.find("/") + 1:].find("/")])
        except:
            #print("Error in day format")
            pass
        else:
            if day > 31:
                raise ValueError("Invalid day value")

        #read year
        try:
            year = int(date.split("/")[-1].strip())
        except:
            #print("Error in year format")
            pass

    #format with month as string
    else:
        #read month
        try:
            month = months.index(date[:date.find(" ")].title()) + 1
        except:
            #print("Error in month format")
            pass
        else:
            if month > 12:
                raise ValueError("Invalid month value")

        #read day
        try:
            day = int(date[date.find(" ") + 1:date.find(",")])
        except:
            #print("Error in day format")
            pass
        else:
            if day > 31:
                raise ValueError("Invalid day value")

        #read year
        try:
            year = int(date[date.find(",") + 1:].strip())
        except:
            #print("Error in year format")
            pass


    return (day, month, year)

#main function
def main():

    while True:
        try:
            day, month, year = read_date(input("Date: "))
        except:
            pass
        else:
            break

    #output date in format YYYY-MM-DD
    print(f"{str(year)}-{nn_format(month)}-{nn_format(day)}")



if __name__ == "__main__":
    main()