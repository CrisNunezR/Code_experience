# TODO

from cs50 import get_float

def main():
    change = get_float('enter owed change: ')

    if change < 0:
        change = get_float('please enter only positive values: ')

    #coins available are quarters (25¢), dimes (10¢), nickels (5¢), and pennies (1¢)
    coins = []

    #takes out 1-dollar bills
    #only_coins = change % 1       #assumes dollar bills are not considered change

    only_coins = change           #assumes dollars must be broken down to quarters

    if only_coins >= 0.25:
        coins.append((100*only_coins / 25) // 1)
        only_coins = 100*only_coins % 25 / 100

    if only_coins >= 0.1:
        coins.append((100*only_coins / 10) // 1)
        only_coins = 100*only_coins % 10 / 100

    if only_coins >= 0.05:
        coins.append((100*only_coins / 5) // 1)
        only_coins = 100*only_coins % 5 / 100

    if only_coins >= 0.01:
        coins.append(100*only_coins)


    print(sum(coins))
    return sum(coins)

    #estimate number of dollars





main()