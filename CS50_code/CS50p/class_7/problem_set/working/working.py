"""
In a file called working.py, implement a function
called convert that expects a str in either of the
12-hour formats below and returns the corresponding
str in 24-hour format (i.e., 9:00 to 17:00).

Expect that AM and PM will be capitalized (with no
periods therein) and that there will be a space before each.
Assume that these times are representative of actual times,
not necessarily 9:00 AM and 5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM

Raise a ValueError instead if the input to convert is not
in either of those formats or if either time is invalid
(e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that
someone’s hours will start ante meridiem and end post meridiem;
someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

Structure working.py as follows, wherein you’re welcome to modify main
and/or implement other functions as you see fit, but you may not import
any other libraries. You’re welcome, but not required, to use re and/or sys.

"""



import re
import sys


def main():
    while True:
        str_ = input("Hours: ").strip()

        if len(str_) >= 7:
            try:
                print(convert(str_))
            except ValueError:
                sys.exit('ValueError')

            else:
                break
        else:
            raise ValueError



def convert(s):
    if work_hours := re.search(r"^(1[0-2]|[0-9])(?:\:)?([0-5][0-9])?\s(AM|PM)\sto\s(1[0-2]|[0-9])(?:\:)?([0-5][0-9])?\s(AM|PM)", s):

        hour_in = "0" + work_hours.group(1) if int(work_hours.group(1)) < 10 else work_hours.group(1)
        min_in = "00" if work_hours.group(2) is None else work_hours.group(2)
        in_AMPM = "" if work_hours.group(3) is None else work_hours.group(3)

        hour_out = "0" + work_hours.group(4) if int(work_hours.group(4)) < 10 else work_hours.group(4)
        min_out = "00" if work_hours.group(5) is None else work_hours.group(5)
        out_AMPM = "" if work_hours.group(6) is None else work_hours.group(6)


        hour_24 = ""

        if in_AMPM == "AM":
            hour_in = "00" if hour_in == "12" else hour_in
            hour_24 = hour_in + ":" + min_in + " to "
        elif in_AMPM == "PM":
            if hour_in == '12':
                hour_24 = hour_in + ":" + min_in + " to "
            else:
                hour_24 = str(int(hour_in) + 12) + ":" + min_in + " to "
        else:
            raise ValueError

        if out_AMPM == "AM":
            hour_out = "00" if hour_out == "12" else hour_out
            hour_24 = hour_24 + hour_out + ":" + min_out
        elif out_AMPM == "PM":
            if hour_out == "12":
                hour_24 = hour_24 + hour_out + ":" + min_out
            else:
                hour_24 = hour_24 + str(int(hour_out) + 12) + ":" + min_out
        else:
            raise ValueError

        return hour_24
    else:
        raise ValueError


if __name__ == "__main__":
    main()