"""
In a file called nutrition.py, implement a program
that prompts consumers users to input a fruit (case-insensitively)
and then outputs the number of calories in one portion of that fruit,
per the FDA’s poster for fruits, which is also available as text.

Capitalization aside, assume that users will input fruits exactly
as written in the poster (e.g., strawberries, not strawberry).
Ignore any input that isn’t a fruit.
"""
import csv

def main():

    fruit = input("Item: ").lower()
    #fruit = fruit[0].upper() + fruit[1:]

    #adjustes the case-sensitivity of the input fruit
    fruit_upper = ""
    for i in range(len(fruit)):
        if i == 0:
            fruit_upper = fruit_upper + fruit[i].upper() #upper cases first char
        elif fruit[i-1] == " ":
            fruit_upper = fruit_upper + fruit[i].upper() #upper cases first char second word
        else:
            fruit_upper = fruit_upper + fruit[i]

    #Option reading from a csv file that seems not to be working with CS50's checker
    """
    with open('nutrition_facts.csv', newline='') as csvfile:
        fieldnames = ['fruit', 'calories']
        fruit_data = csv.DictReader(csvfile, fieldnames = fieldnames, delimiter = ',')

        for i in fruit_data:
            if i['fruit'] == fruit_upper:
                cals = i['calories']
                break

        csvfile.close()
    """

    fruits = {
        "Apple" : 130,
        "Avocado" : 50,
        "Banana": 110,
        "Cantaloupe":50,
        "Grapefruit": 60,
        "Grapes" : 90,
        "Honeydew Melon":50,
        "Kiwifruit":90,
        "Lemon":15,
        "Lime":20,
        "Nectarine":60,
        "Orange":80,
        "Peach":60,
        "Pear":100,
        "Pineapple":50,
        "Plums":70,
        "Strawberries":50,
        "Sweet Cherries":100,
        "Tangerine":50,
        "Watermelon":80
    }

    try:
        print('Calories:', fruits[fruit_upper])
    except:
        return -1


main()