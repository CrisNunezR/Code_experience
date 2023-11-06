class person:
    def __init__(self, name = 'mat', age = 15):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

p1 = person('john', 35)

print(p1)

print(p1.name + ' is ' + str(p1.age) + ' years old.')

print(p2.name + ' is ' + str(p2.age) + ' years old.')
