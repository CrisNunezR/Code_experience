

#x = input("x: ")
#y = input("y: ")
#print(x + y)

#x = int(input("x: "))
#y = int(input("y: "))
#print(x + y)

###################################
##Working with lists (arrays) [] in Python

#creating a list
#nums = list()
#print(nums)

#creating a list with range
#nums = [x for x in range(500)]
#print(nums)

#appending values
#nums = [1,2,3,4]
#print(nums)
#nums.append(5)
#print(nums)

#inserting values
#nums = [1,2,3,5]
#print(nums)
#nums.insert(3, 4)
#print(nums)

#print(nums[len(nums)-1:])
#print(nums)


###################################
#Working with Tuples ()

#defining a Tuple:
#presidents = [
#    ("G. Washington", 1789),
#    ("J. Adams", 1979),
#    ("T. Jefferson", 1801),
#    ('J. Madison', 1809)
#]

#printing out values from tuple
#for prez, year in presidents:
#    print("In {1}, {0} took office".format(prez, year))

        #notice that {i} defines the element we used from the Tuple
            #{0}: 1st element (president)
            #{1}: 2nd element (year)
        #also notice that the method
        # .format defines the names of variables in the tuple

###################################
#Working with Dictionaries {}

#define a dictionary
pizzas = {
    "cheese": 9,
    'pepperoni': 10,
    'vegetable': 11,
    'buffalo chicken': 12
}

print('cheese: ', pizzas['cheese'])

pizzas['cheese'] = 10

print('cheese: ', pizzas['cheese'])

pizzas['bacon'] = 4

print(pizzas)

#iterating over a dictionary
for i in pizzas:
    print(i)

#to access the values within the dictionary, we need to transform it
#to a list using the .items() method

for x, y in pizzas.items():
    print(x, y)

for x, y in pizzas.items():
    print("A whole  {} pizza costs ${}".format(x, y))

for x, y in pizzas.items():
    print("A whole " + x + " pizza costs $" + str(y))

text = "here.   "
print(text.strip() + "s")