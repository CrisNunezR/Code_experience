"""
Suppose that a machine sells bottles of Coca-Cola (Coke)
for 50 cents and only accepts coins in these denominations:
    25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the
user to insert a coin, one at a time, each time informing the user
of the amount due. Once the user has inputted at least 50 cents,
output how many cents in change the user is owed. Assume that the
user will only input integers, and ignore any integer that isn’t
an accepted denomination.
"""

#validates the denomination of the coin
def input_coin(coin_: str) -> int:
      coin_ = int(coin_)
      if coin_ in [5, 10, 25]:
        return coin_
      else:
        return 0



def main():

    accu = 0

    while accu < 50:
        print("Amount Due:", 50 - accu)
        coin = input_coin(input("Inser Coin:"))
        accu += coin

    print("Change Owed:", accu - 50)#, end = "\n")


main()