"""
Implement a program that prompts the user for items,
one per line, until the user inputs control-d
(which is a common way of ending one’s input to a program).

Then output the user’s grocery list in all uppercase,
sorted alphabetically by item, prefixing each line with
the number of times the user inputted that item. No need to pluralize the items.
Treat the user’s input case-insensitively.

"""



def main():

    groc_dic = {}

    #prompts user for items until ctrl-D
    while True:
        try:
            item = input().upper()
        except EOFError:
            break
        else:
            #increases count of item in dictionary or adds item in dictionary if not in there (except)
            try:
                groc_dic[item] = groc_dic[item] + 1
            except KeyError:
                groc_dic[item] = 1

    #print out list with number of items in alphabetical order (sorted(list))
    for item_ in sorted(list(groc_dic)):
        print(groc_dic[item_], item_)


if __name__ == "__main__":
    main()