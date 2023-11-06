"""
In meal.py, implement a program that prompts the user for a time
and outputs whether it’s breakfast time, lunch time, or dinner time.
If it’s not time for a meal, don’t output anything at all.

Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##.
And assume that each meal’s time range is inclusive. For instance, whether it’s
7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

Structure your program per the below, wherein convert is a function
(that can be called by main) that converts time, a str in 24-hour format,
to the corresponding number of hours as a float. For instance, given a time
like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).

Suppose that you’re in a country where it’s customary to eat
breakfast between 7:00 and 8:00,
lunch between 12:00 and 13:00,
and dinner between 18:00 and 19:00

"""



def main():

    time_ = input("What time is it? ").replace(" ", "")
    time_dec = round(convert(time_),1)
    #print(time_dec)

    if 7 <= time_dec <= 8:
        print("breakfast time")
    elif 12 <= time_dec <= 13:
        print("lunch time")
    elif 18 <= time_dec <= 19:
        print("dinner time")


#converts time in str format to a float
def convert(time: str) -> float:

    hr_sep = find_sep(time)

    if is_am_pm(time):
        #complete for am_pm format
        if time.find('p.m') > -1:
            if float(time[:hr_sep]) == 12:
                return (float(time[:hr_sep]) + float(time[hr_sep+1:-2])/60)
            else:
                return (float(time[:hr_sep]) + 12 + float(time[hr_sep+1:-2])/60)
        else:
            #notice that we already checked for 'am-pm' so we can assume there's no other option
            if float(time[:hr_sep]) == 12:
                return (float(time[hr_sep+1:-2])/60) #hr is changed from 12am to 0hrs
            else:
                return (float(time[:hr_sep]) + float(time[hr_sep+1:-2])/60)
    else:
        #complete for 24hrs format
        return (float(time[:hr_sep]) + float(time[hr_sep+1:])/60)


#identifies am/pm format:
def is_am_pm(t: str) -> bool:
    if t.find('a.m.') != -1 or t.find('p.m.') != -1:
        return True
    else:
        return False

#finds ':' char and returns position
def find_sep(str_: str) -> int:
    return str_.find(":")

if __name__ == "__main__":
    main()